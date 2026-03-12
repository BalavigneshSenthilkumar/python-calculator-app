import sqlite3

DB_NAME = "calculator.db"

def init_db():
    conn = sqlite3.connect("mypython.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT,
            result TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(expression, result):
    conn = sqlite3.connect("mypython.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (expression, result) VALUES (?, ?)", (expression, result))
    conn.commit()
    conn.close()

def fetch_history():
    conn = sqlite3.connect("mypython.db")
    cursor = conn.cursor()
    cursor.execute("SELECT expression, result FROM history ORDER BY id DESC")
    records = cursor.fetchall()
    conn.close()
    return records
