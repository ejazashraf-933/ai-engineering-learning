import re
import pytest

BLOCKED = ["drop", "delete", "update", "insert", "alter"]

def is_safe_sql(query: str) -> bool:
    q = query.lower()
    return not any(re.search(rf"\b{word}\b", q) for word in BLOCKED)

@pytest.mark.parametrize("query", ["DELETE FROM x", "insert into y", "Alter table z"])
def test_dangerous_is_blocked(query):
    assert is_safe_sql(query) is False