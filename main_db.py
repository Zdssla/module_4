import sqlite3


class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

def create_table_users(cursor):
    command = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    gender TEXT);
    """
    cursor.execute(command)

def add_user(cursor, user):
    command = """
    INSERT INTO users (name, surname, gender) VALUES (?, ?, ?);
    """
    cursor.execute(command, (user.name, user.surname, user.gender))

def get_users_list(cursor):
    command = """
    SELECT * FROM users;
    """
    users = cursor.execute(command).fetchall()
    print(users)

def get_user(cursor, user_id):
    command = """
    SELECT * FROM users WHERE id = ?;
    """
    user = cursor.execute(command, (user_id,)).fetchall()
    print(user)

def delete_users(cursor):
    command = """
    DELETE FROM users;
    """
    cursor.execute(command)

def update_user_name(cursor, user_id, new_name):
    command = """
    UPDATE users SET name = ? WHERE id = ?;
    """
    cursor.execute(command, (new_name, user_id))

def delete_id(cursor, user_id):
    command = """
    DELETE FROM users WHERE id = ?;
    """
    cursor.execute(command, (user_id,)).fetchall()

def get_gender(cursor, gender):
    command = """
    SELECT name FROM users WHERE gender = ?;
    """
    gender_1 = cursor.execute(command,(gender,)).fetchall()
    print(gender_1)

if __name__ == '__main__':
    with sqlite3.connect('data.db') as cursor:
        create_table_users(cursor) # создание таблицы 
        delete_users(cursor) # удаление всех данных из таблицы, если они есть 
        # наполнение таблицы данными
        add_user(cursor, User('Максим', 'Иванов', 'male'))
        add_user(cursor, User('Владимир', 'Петров', 'male'))
        add_user(cursor, User('Екатерина', 'Кузнецова', 'female'))
        # вывод пользователей
        get_users_list(cursor)
        get_user(cursor, 1)  
        update_user_name(cursor, 1, 'Денис')
        get_user(cursor, 1)
        get_gender(cursor, 'male')
        delete_id(cursor, 2)
        get_users_list(cursor)