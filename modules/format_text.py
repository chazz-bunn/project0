def format_text(text):
    text = text.lower()
    text = "".join([e if e.isalpha() else "" for e in text])
    return text