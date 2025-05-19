def score(output: str, context) -> float:
    keyword = context.get("config", {}).get("keyword", "香蕉")
    print("bannan" if keyword == "香蕉" else "guava")
    return 1.0 if (keyword in output ) else 0.0

def get_assert(output, context):
    keyword = context.get("config", {}).get("keyword", "香蕉")
    return 1.0 if (keyword in output ) else 0.0
