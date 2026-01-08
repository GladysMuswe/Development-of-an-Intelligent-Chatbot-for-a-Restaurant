# Development-of-an-Intelligent-Chatbot-for-a-Restaurant
An AI-powered restaurant chatbot developed in Python to automate table reservations, menu inquiries, food ordering and customer interaction. Built as an academic project using NLP concepts, SQLite and rule-based dialogue management, with usability results aligned to a bachelor’s thesis on intelligent chatbots for restaurants.

# Intelligent Restaurant Chatbot (Python)

## 📌 Project Overview
This project is an intelligent chatbot developed for a restaurant environment.  
It automates common customer interactions such as table reservations, menu inquiries, vegan/allergen checks, and basic food ordering.

The chatbot was developed as part of a Bachelor’s thesis titled:

“Development of an Intelligent Chatbot for a Restaurant”**

The system demonstrates how Natural Language Processing (NLP) and lightweight backend technologies can be applied to improve customer service efficiency in the hospitality industry.

---

## 🎯 Features
- Greeting and small talk handling
- Menu display and vegan food filtering
- Table reservation with confirmation
- Food order placement (simulated)
- SQLite database integration
- Fast response time and simple dialogue flow
- Usability evaluation results included

---

## 🛠️ Technologies Used
- Programming Language:Python 3
- Database: SQLite
- Libraries: Pandas, Scikit-learn, NLTK
- Architecture: Rule-based NLP + backend logic
- Environment: Local execution (offline)

---

## 📂 Project Structure
restaurant_chatbot/
│
├── app.py # Main chatbot application
├── chatbot_logic.py # Intent handling and responses
├── database.py # SQLite database setup
├── evaluation.py # Usability evaluation results
├── requirements.txt
├── README.md
└── data/
└── menu.csv # Restaurant menu dataset


---

## ▶️ How to Run the Project

1. Install dependencies:
```bash
pip install -r requirements.txt

2. Initialize the database:
python database.py

3. Start Chatbot
python app.py

4. View usability evaluation results
python evaluation.py


