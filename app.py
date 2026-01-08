from chatbot_logic import *
print(greet())
while True:
    u=input("You: ").lower()
    if "menu" in u: print("Bot:",get_menu())
    elif "vegan" in u: print("Bot:",vegan_menu())
    elif "book" in u:
        p=input("People: "); t=input("Time: ")
        print("Bot:",book_table(p,t))
    elif "order" in u:
        i=input("Items: ")
        print("Bot:",order_food(i))
    elif "bye" in u:
        print("Bot: Goodbye!"); break
    else: print("Bot:",fallback())
