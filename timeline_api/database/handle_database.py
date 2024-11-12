import sqlite3

conn = sqlite3.connect('./timeline_database')

def init():
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS timeline (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            owner INTEGER,
            thumbnail TEXT,
            contents TEXT,
            farm INTEGER
            )
    ''')
    conn.commit()

def get_timeline_list():
    cur = conn.cursor()
    cur.execute("SELECT * FROM timeline")
    res = cur.fetchall()
    print(res)
    return res

def add_timeline(title, owner, thumbnail, contents, farm):
    cur = conn.cursor()
    cur.execute("INSERT INTO timeline (title, owner, thumbnail, contents, farm) VALUES (?, ?, ?, ?, ?)", (title, owner, thumbnail, contents, farm))
    conn.commit()
    return 0

init()