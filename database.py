import sqlite3
def init_db():
    conn = sqlite3.connect("restaurant.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS reservations (id INTEGER PRIMARY KEY AUTOINCREMENT, people INTEGER, time TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, items TEXT)")
    conn.commit(); conn.close()
if __name__=='__main__': init_db()
