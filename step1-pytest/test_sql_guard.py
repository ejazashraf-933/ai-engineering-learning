from sql_guard import is_safe_sql
import pytest

def test_select_is_safe():
    assert is_safe_sql("SELECT * FROM cards") is True

def test_drop_is_blocked():
    assert is_safe_sql("DROP TABLE cards") is False

def test_table_named_updates_is_safe():
    assert is_safe_sql("SELECT * FROM updates_log") is True

@pytest.mark.parametrize("query", ["DELETE FROM x", "insert into y", "Alter table z"])
def test_dangerous_is_blocked(query):
    assert is_safe_sql(query) is False