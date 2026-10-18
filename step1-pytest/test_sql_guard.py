from sql_guard import is_safe_sql

def test_select_is_safe():
    assert is_safe_sql("SELECT * FROM cards") is True

def test_drop_is_blocked():
    assert is_safe_sql("DROP TABLE cards") is False

def test_table_named_updates_is_safe():
    assert is_safe_sql("SELECT * FROM updates_log") is True
