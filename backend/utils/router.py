def route_query(query):
    if any(word in query.lower() for word in ["calculate", "solve"]):
        return "math"
    elif "law" in query.lower():
        return "legal"
    else:
        return "general"