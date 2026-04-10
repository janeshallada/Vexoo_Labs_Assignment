def summarize(text):
    sentences = text.split(".")
    return ". ".join(sentences[:2])