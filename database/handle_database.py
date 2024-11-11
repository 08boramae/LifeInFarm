import sqlite3

conn = sqlite3.connect('./lifeinfarm_database')

def init():
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS timeline (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()