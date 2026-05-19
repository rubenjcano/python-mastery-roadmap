"""
Exercise 01 — LLM APIs & Prompting
=====================================
Requires: pip install anthropic python-dotenv
Set ANTHROPIC_API_KEY in a .env file.
"""
import os
from dotenv import load_dotenv
import anthropic

load_dotenv()


def get_client() -> anthropic.Anthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set in .env")
    return anthropic.Anthropic(api_key=api_key)


# ── Exercise 1: Basic Q&A ─────────────────────────────────────────────────
def ask_question(question: str, system_prompt: str = "") -> str:
    """Send a question to Claude and return the text response.
    
    Hint: client.messages.create(), message.content[0].text
    """
    # TODO
    ...


# ── Exercise 2: Conversation with memory ─────────────────────────────────
def multi_turn_chat(turns: list[tuple[str, str]]) -> str:
    """Send a multi-turn conversation and return last assistant response.
    
    turns: list of (role, content) — role is "user" or "assistant"
    Append a final user message with "Summarise what we discussed."
    """
    # TODO
    ...


# ── Exercise 3: Structured extraction ────────────────────────────────────
def extract_invoice_data(invoice_text: str) -> dict:
    """Extract structured data from invoice text.
    
    Return a dict with keys: vendor, date, total_amount, currency, line_items
    Use prompting to get JSON output, then parse it.
    
    Hint: json.loads(), instruct the model to return ONLY JSON
    """
    import json
    # TODO
    ...


# ── Exercise 4: Streaming ─────────────────────────────────────────────────
def stream_summary(text: str) -> None:
    """Print a streaming summary of the given text, word by word."""
    # TODO: use client.messages.stream()
    ...


# ─── Demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Exercise 1
    ans = ask_question("What is DuckDB in one sentence?")
    print(f"Q&A: {ans}\n")

    # Exercise 3
    invoice = """
    Invoice #2024-001
    Vendor: DataTools GmbH
    Date: 2024-03-15
    Items:
    - PySpark Training: €1,200.00
    - dbt Workshop: €800.00
    Total: €2,000.00 EUR
    """
    data = extract_invoice_data(invoice)
    print(f"Extracted: {data}\n")
