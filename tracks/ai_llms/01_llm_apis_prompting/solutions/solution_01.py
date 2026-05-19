"""
Solution 01 — LLM APIs & Prompting
"""
import os, json
from dotenv import load_dotenv
import anthropic

load_dotenv()

def get_client() -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def ask_question(question: str, system_prompt: str = "") -> str:
    client = get_client()
    kwargs = dict(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[{"role": "user", "content": question}],
    )
    if system_prompt:
        kwargs["system"] = system_prompt
    msg = client.messages.create(**kwargs)
    return msg.content[0].text


def multi_turn_chat(turns: list[tuple[str, str]]) -> str:
    client = get_client()
    messages = [{"role": role, "content": content} for role, content in turns]
    messages.append({"role": "user", "content": "Summarise what we discussed."})
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=messages,
    )
    return msg.content[0].text


def extract_invoice_data(invoice_text: str) -> dict:
    client = get_client()
    prompt = (
        "Extract the following fields from the invoice below.\n"
        "Return ONLY valid JSON with keys: vendor, date, total_amount, currency, line_items.\n"
        "line_items should be a list of {description, amount}.\n"
        "No markdown, no explanation — pure JSON only.\n\n"
        f"Invoice:\n{invoice_text}"
    )
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    return json.loads(msg.content[0].text)


def stream_summary(text: str) -> None:
    client = get_client()
    with client.messages.stream(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[{"role": "user", "content": f"Summarise in 3 sentences:\n{text}"}],
    ) as stream:
        for chunk in stream.text_stream:
            print(chunk, end="", flush=True)
    print()
