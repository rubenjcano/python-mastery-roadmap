def word_frequency(text: str) -> dict[str, int]:
    """Count frequency of each word (lowercased, stripped of punctuation).
    
    Example: word_frequency("Hello world hello")
    → {"hello": 2, "world": 1}
    
    Hint: str.split(), str.lower(), str.strip(".,!?")
    Use a dict comprehension or Counter.
    """
    
    text_list = text.split()
    for i in text_list:
        i.lower
    return text_list

text = "Hello world hello"
print(word_frequency(text))

    