import sqlite3

def init_db():
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()

    #create an employee table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EMPLOYEES (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        DEPARTMENT TEXT NOT NULL,
        SALARY REAL NOT NULL,
        HIRE_DATE TEXT NOT NULL
    );
    """)
    #Insert data
    cursor.executemany("""
    INSERT INTO EMPLOYEES(NAME, DEPARTMENT, SALARY, HIRE_DATE) VALUES (?,?,?,?)
    """, [("Alice","Sales", 50000, "2021-01-15"),
          ("Bob","Engineering", 70000, "2020-06-10"),
          ("Charlie", "Marketing", 60000, "2022-03-10"),
          ("Frank","HR", 85000,"2014-02-22"),
          ("Abhimaan", "Operations",100000,"2011-04-11"),
          ("Raj","Finance", 90000,"2017-01-14"),
          ("Olivia","Customer Service", 43000, "2018-07-16"),
          ("Abhai", "R&D", 110000, "2011-06-23"),
          ("Priya", "Engineering", 95000,"2016-06-17"),
          ("Sam", "IT", 79000, " 2011-09-16"),
          ("Naina", "Sales",55000, "2013-11-17"),
          ("Ian","Customer Service", 80000,"2013-07-15"),
          ("Alex", "HR", 80000, "2022-06-20"),
          ("Stephen","Finance",75000, "2020-05-05"),
          ("John", "IT", 45000, "2022-08-12")
    ])

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DEPARTMENTS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        MANAGER TEXT NOT NULL);
    """)

    cursor.executemany("""
    INSERT INTO DEPARTMENTS(NAME, MANAGER) VALUES (?,?)
    """,[("Sales","Alice"),
         ("Engineering","Bob"),
         ("Marketing","Charlie"),
         ("HR","Frank"),
         ("Operations","Abhimaan"),
         ("Finance","Raj"),
         ("Customer Service","Olivia"),
         ("R&D","Abhai"),
         ("IT","Sam")])
    # Commit and close
    connection.commit()
    connection.close()

    print("Database setup completed.")

if __name__ == "__main__":
    init_db()