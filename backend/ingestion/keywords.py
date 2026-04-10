def extract_keywords(text):
    words = text.split()
    return list(set(words[:10]))