import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv
import os

load_dotenv()
conn = None

try:
    conn = psycopg2.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        port = os.getenv('DB_PORT'),
        dbname = os.getenv('DB_NAME')
    )
    print(f"Connected to database.\n")
except Exception as e:
    print(f"Connection failed.", e)

if conn is None:
    print("App stopped: no database connection")
    exit()

cursor = conn.cursor(cursor_factory=DictCursor)


class UserToDo():
    def __init__(self, name='New User'):
        self.name = name

    def create_task(self, title: str, description: str):
        if not title:
            print("You need to add a title for your task!")
            return None

        self.title = title
        self.description = description

        sql = f"INSERT INTO todo_list(title, description) VALUES(%s, %s)"

        try:
            cursor.execute(sql, (title, description))
            conn.commit()
            print('Your task was succesfully added.\n')
        except Exception as e:
            print("Your task wasn't create", e)


    def delete_task(self, id):
        if not id:
            print("Type id of your task")
            return None

        sql = f"DELETE FROM todo_list WHERE id = %s"
        try:
            cursor.execute(sql, (id,))
            conn.commit()
            print('Your task was deleted\n')
        except Exception as e:
            print("Ooops...Something wrong.", e)

    def show_tasks(self):
        cursor.execute('SELECT * FROM todo_list')
        result = cursor.fetchall()

        for row in result:
            print(row['id'], row['title'].upper())
            print(row['description'])

    def update_task(self, id, title: str, description: str):
        if not id:
            print('Type id of your task.')
            return None

        self.title = title
        self.description = description

        sql = f"UPDATE todo_list SET title = %s, description = %s WHERE id = %s"

        try:
            cursor.execute(sql, (title, description, id))
            conn.commit()
            print('Your task was succesfully updated.\n')
        except Exception as e:
            print("Your task wasn't updated", e)




user = UserToDo()


cursor.close()
conn.close()


# sql = f"INSERT INTO news(title, preview) VALUES(%s, %s)"
# cursor.execute(sql, (title, preview))
# conn.commit()
#
# cursor.execute('SELECT * FROM news')
# result = cursor.fetchall()
#
# print(result)
#