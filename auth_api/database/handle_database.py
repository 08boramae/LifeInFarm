import sqlite3

conn = sqlite3.connect('./auth_database')

def init():
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            id TEXT UNIQUE,
            pw TEXT,
            location TEXT,
        )
    ''')
    conn.commit()

def login(id, pw):
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE id = ? AND pw = ?", (id, pw))
    res = cur.fetchone()
    if res:
        return 1
    else:
        return 0