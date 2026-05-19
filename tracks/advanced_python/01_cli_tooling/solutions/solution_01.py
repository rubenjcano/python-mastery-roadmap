"""
Solution 01 — CLI Tooling
"""
import csv
from collections import Counter
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(name="csvstats", help="CSV statistics CLI tool")
console = Console()


def _read_csv(filepath: Path) -> list[dict]:
    if not filepath.exists():
        raise typer.BadParameter(f"File not found: {filepath}")
    with filepath.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


@app.command()
def stats(
    filepath: Path = typer.Argument(...),
    columns: list[str] = typer.Option(None, "--col", "-c"),
    top: int = typer.Option(5, "--top", "-n"),
):
    """Show column statistics for a CSV file."""
    rows = _read_csv(filepath)
    if not rows:
        console.print("[yellow]File is empty[/yellow]")
        raise typer.Exit()

    cols = columns or list(rows[0].keys())

    table = Table(title=f"Stats: {filepath.name}", show_lines=True)
    table.add_column("Column", style="bold cyan")
    table.add_column("Unique Values", justify="right")
    table.add_column("Most Common", style="green")
    table.add_column("Count", justify="right")

    for col in cols:
        if col not in rows[0]:
            console.print(f"[red]Column '{col}' not found[/red]")
            continue
        values = [r[col] for r in rows]
        counter = Counter(values)
        most_common, count = counter.most_common(1)[0]
        table.add_row(col, str(len(counter)), most_common, str(count))

    console.print(table)


@app.command()
def preview(
    filepath: Path = typer.Argument(...),
    rows: int = typer.Option(10, "--rows", "-r"),
):
    """Preview the first N rows of a CSV file."""
    data = _read_csv(filepath)[:rows]
    if not data:
        console.print("[yellow]File is empty[/yellow]")
        return

    table = Table(title=f"Preview: {filepath.name} (first {rows} rows)", show_lines=True)
    for col in data[0].keys():
        table.add_column(col, style="cyan", overflow="fold")
    for row in data:
        table.add_row(*row.values())
    console.print(table)


if __name__ == "__main__":
    app()
