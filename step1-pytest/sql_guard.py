import re
BLOCKED = ["drop", "delete", "update", "insert", "alter"]

def is_safe_sql(query: str) -> bool:
    q = query.lower()
    return not any(re.search(rf"\b{word}\b", q) for word in BLOCKED)

