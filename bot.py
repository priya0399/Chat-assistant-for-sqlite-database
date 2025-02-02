import sqlite3
import nltk
import tkinter as tk
from SQLite_db import init_db


# Download necessary NLTK data
nltk.download("punkt")

# Initialize database
def init_db():
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EMPLOYEES (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        DEPARTMENT TEXT NOT NULL,
        SALARY REAL NOT NULL,
        HIRE_DATE TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DEPARTMENTS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        MANAGER TEXT NOT NULL
    );
    """)

    connection.commit()
    connection.close()

# Queries for chatbot
queries = {
    "all the employees"or "show all employees": "SELECT * FROM EMPLOYEES",
    "all the departments": "SELECT * FROM DEPARTMENTS",
    "employees with salary more than 80k": "SELECT * FROM EMPLOYEES WHERE SALARY > 80000",
    "total number of employees" or "total employees": "SELECT COUNT(*) FROM EMPLOYEES",
    "average salary": "SELECT AVG(SALARY) FROM EMPLOYEES",
    "highest salary": "SELECT * FROM EMPLOYEES ORDER BY SALARY DESC LIMIT 1",
    "employees in engineering": "SELECT * FROM EMPLOYEES WHERE DEPARTMENT = 'Engineering'",
    "total salary expense": "SELECT SUM(SALARY) FROM EMPLOYEES",
    "employees count by department": "SELECT DEPARTMENT, COUNT(*) FROM EMPLOYEES GROUP BY DEPARTMENT",
    "employees hired after" : "SELECT * FROM EMPLOYEES WHERE HIRE_DATE >?",
    "manager of department" :"SELECT Manager FROM Department WHERE Department = ?",
    "total salary expense for the department":  "SELECT SUM(Salary) FROM Employee WHERE Department = ?",

}

# Function to process user input
def convert_to_sql(user_input):
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()
    
    user_input = user_input.lower()

    for key, query in queries.items():
        if key in user_input:
            cursor.execute(query)
            result = cursor.fetchall()
            connection.close()
            return result if result else "No results found."


    connection.close()
    return "I am not sure about that query."

# Function to handle chat input
def chat():
    user_message = entry.get()
    chat_log.insert(tk.END, f"You: {user_message}\n")

    response = convert_to_sql(user_message)
    
    if isinstance(response, list):
        response = "\n".join(str(row) for row in response)
    chat_log.insert(tk.END, f"Bot: {response}\n\n")

    entry.delete(0, tk.END)

# GUI using Tkinter
root = tk.Tk()
root.title("SQLite Chatbot")

chat_log = tk.Text(root, height=20, width=80)
chat_log.pack()

entry = tk.Entry(root, width=80)
entry.pack()

send_button = tk.Button(root, text="Send", command=chat)
send_button.pack()

init_db()
root.mainloop()
