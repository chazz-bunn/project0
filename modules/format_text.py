#used to format input text to be all lowercase and contain no punctuation
def format_text(text):
    text = text.lower()
    text = "".join([e if e.isalnum() or e == " " else "" for e in text])
    return text