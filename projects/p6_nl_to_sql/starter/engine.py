"""
P6 — NL to SQL Engine — STARTER
"""
from dataclasses import dataclass
import duckdb
import sqlglot
import anthropic


@dataclass
class QueryResult:
    sql: str
    columns: list[str]
    rows: list[tuple]
    explanation: str
    error: str | None = None


def get_schema_context(conn: duckdb.DuckDBPyConnection) -> str:
    """Return a string describing all tables and their columns.
    
    Hint: conn.execute("SHOW TABLES").fetchall()
          conn.execute(f"DESCRIBE {table}").fetchall()
    """
    # TODO
    ...


def generate_sql(question: str, schema_context: str, error_hint: str = "") -> str:
    """Use Claude to generate SQL from a natural language question.
    
    Include the schema_context in the prompt so Claude knows the tables.
    If error_hint is provided, include it so Claude can fix the previous attempt.
    Return ONLY the SQL string (no markdown, no explanation).
    """
    # TODO
    ...


def validate_sql(sql: str) -> tuple[bool, str]:
    """Validate SQL using sqlglot. Return (is_valid, error_message)."""
    # TODO: sqlglot.parse(sql, error_level=sqlglot.ErrorLevel.RAISE)
    ...


def execute_with_retry(conn, question: str, schema_context: str, max_retries: int = 3) -> QueryResult:
    """Generate SQL, validate, execute. Retry on error with feedback.
    
    Loop:
    1. Generate SQL
    2. Validate with sqlglot
    3. Execute against DuckDB
    4. If error, retry with the error message as hint
    """
    # TODO
    ...


def explain_results(sql: str, columns: list[str], rows: list[tuple], question: str) -> str:
    """Use Claude to write a 2-3 sentence explanation of the query results."""
    # TODO
    ...
