"""
Exercise 01 — CLI Tooling with Typer + Rich
============================================
Build a CLI tool that processes CSV files and shows stats.

Run: python exercise_01.py --help
"""
import typer
from rich.console import Console
from rich.table import Table
from pathlib import Path

app = typer.Typer(name="csvstats", help="CSV statistics CLI tool")
console = Console()


@app.command()
def stats(
    filepath: Path = typer.Argument(..., help="Path to CSV file"),
    columns: list[str] = typer.Option(None, "--col", "-c", help="Columns to analyse"),
    top: int = typer.Option(5, "--top", "-n", help="Show top N values per column"),
):
    """Show statistics for a CSV file using Rich tables."""
    # TODO:
    # 1. Check file exists, raise typer.BadParameter if not
    # 2. Read CSV with csv.DictReader
    # 3. For each column (or --col selection):
    #    - Count values, find most common
    #    - Print a Rich Table with: column name, unique values, most common value, count
    # 4. Use console.print() with Rich markup for colour
    ...


@app.command()
def preview(
    filepath: Path = typer.Argument(..., help="Path to CSV file"),
    rows: int = typer.Option(10, "--rows", "-r", help="Number of rows to show"),
):
    """Preview the first N rows of a CSV file as a Rich table."""
    # TODO: read CSV, display as rich.table.Table
    ...


if __name__ == "__main__":
    app()
