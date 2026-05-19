# LLM APIs & Prompting

## Anthropic SDK
```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

# Simple message
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explain PySpark in one paragraph."}],
)
print(message.content[0].text)

# System prompt + conversation history
messages = [
    {"role": "user",      "content": "My name is Ruben."},
    {"role": "assistant", "content": "Nice to meet you, Ruben!"},
    {"role": "user",      "content": "What's my name?"},
]
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=256,
    system="You are a helpful assistant with perfect memory.",
    messages=messages,
)
```

## Streaming
```python
with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write a haiku about data."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

## Prompting techniques

### Chain-of-thought
```
System: You are an expert analyst. Think step by step before answering.
User: What's the profit margin if revenue is €12,000 and costs are €8,400?

→ Better than asking directly — model shows its work
```

### Few-shot prompting
```
User: Classify sentiment as POSITIVE/NEGATIVE/NEUTRAL.

Examples:
"I love this product!" → POSITIVE
"It's okay, nothing special." → NEUTRAL
"Complete waste of money." → NEGATIVE

Now classify: "The packaging was fine but the product broke in a week."
```

### Structured output prompt
```
Extract data as JSON with keys: name, date, amount, currency.
Respond ONLY with valid JSON, no markdown fences.
```

## Token counting
```python
# Always estimate before sending large prompts
response = client.messages.create(...)
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
print(f"Cost estimate: €{response.usage.input_tokens * 0.000003:.4f}")
```
