import sqlite3

conn = sqlite3.connect('./auth_database')

def init():
    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE IF NOT EXISTS user (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            id TEXT UNIQUE,
            name TEXT,
            pw TEXT,
            location TEXT)''')
    conn.commit()

def login(id, pw):
    try:
        cur = conn.cursor()
        cur.execute("SELECT uid, id, name FROM user WHERE id = ? AND pw = ?", (id, pw))
        res = cur.fetchone()
        return res
    except:
        return None

def add_user(id, name, pw, location):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO user (id, name, pw, location) VALUES (?, ?, ?, ?)", (id, name, pw, location))
        conn.commit()
        return 1
    except:
        conn.commit()
        return 0

def get_user_by_username(username):
    cur = conn.cursor()
    cur.execute("SELECT uid, id, name FROM user WHERE id = ?", (username,))
    res = cur.fetchone()
    return res

init()