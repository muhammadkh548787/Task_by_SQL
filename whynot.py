import psycopg2

print("1. Registration")
print("2. Add task")
print("3. Delete task")
print("4. Show tasks")


conn = psycopg2.connect(
    host="localhost",
    database="hello",
    user="postgres",
    password="0199"
)

cursor = conn.cursor()



run = True
while run:
    x = input("Choose your choice: ")

    if x == "1":
        id = input("Enter the id: ")
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = input("Enter the password: ")
        insert = f"""INSERT INTO users (id, username, email, password)
        VALUES ({id}, '{username}', '{email}', '{password}')"""
        values = ({id}, '{username}', '{email}', '{password}')
        cursor.execute(insert, values)
        conn.commit()
        cursor.close()
        conn.close()
    elif x == "2":
        id = input("Enter the task of id: ")
        title = input("Enter the task title: ")
        description = input("Enter the description of the task: : ")
        completed = input("Is your task completed: ")
        username = input("Enter the username: ")
        insert_data = f"""INSERT INTO tasks (id, title, description, completed, username)
        VALUES ({id}, '{title}', '{description}', '{completed}', '{username}')"""
        values = ({id}, '{title}', '{description}', '{completed}', '{username}')
        cursor.execute(insert_data, values)
        conn.commit()
        cursor.close()
        conn.close()
    
    elif x == "3":
        udalit = input("Enter your username: ")
        cursor.execute(f"DELETE FROM users WHERE username = '{udalit}'")
        cursor.execute(f"DELETE FROM tasks WHERE username = '{udalit}'")
        conn.commit()
        cursor.close()
        conn.close() 


    elif x == "4":
        tables = input("Which table you want to see(tasks/users): ")
        cursor.execute(f"SELECT  FROM {tables}") 

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        conn.commit()
        cursor.close()
        conn.close()

