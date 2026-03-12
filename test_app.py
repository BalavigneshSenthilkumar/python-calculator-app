import pytest
from db import init_db, save_to_db, fetch_history

def test_db_insert_and_fetch():
    init_db()
    save_to_db("2+2", "4")
    history = fetch_history()
    assert ("2+2", "4") in history
