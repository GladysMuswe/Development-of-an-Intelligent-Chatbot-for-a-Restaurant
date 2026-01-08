import pandas as pd, sqlite3
menu = pd.read_csv("data/menu.csv")
def greet(): return "Hello! Welcome to FoodEase Bistro. How can I help you today?"
def get_menu(): return "\n".join(menu["name"])
def vegan_menu(): return ", ".join(menu[menu["vegan"]=="Yes"]["name"])
def book_table(p,t):
    conn=sqlite3.connect("restaurant.db");cur=conn.cursor()
    cur.execute("INSERT INTO reservations (people,time) VALUES (?,?)",(p,t))
    conn.commit();conn.close()
    return f"Table for {p} at {t} booked."
def order_food(i):
    conn=sqlite3.connect("restaurant.db");cur=conn.cursor()
    cur.execute("INSERT INTO orders (items) VALUES (?)",(i,))
    conn.commit();conn.close()
    return f"Order placed: {i}"
def fallback(): return "Sorry, I didn’t understand that."
