# import sqlite3
#
# conn = sqlite3.connect("mydb.db")  # 1. Открываем соединение
# cursor = conn.cursor()  # 2. Создаём курсор
#
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER
#     )
# """)  # 3. Выполняем запрос
#
# conn.commit()  # 4. Фиксируем изменения
#
# conn.close()  # 5. Закрываем соединение

# import sqlite3
#
# conn = sqlite3.connect("mydb.db")
# cursor = conn.cursor()
#
# try:
#     cursor.execute("BEGIN TRANSACTION")  # Начинаем транзакцию
#     cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
#     conn.commit()
#     cursor.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))
#
#     raise Exception("Что-то пошло не так!")  # Искусственно создаём ошибку
#     conn.commit()  # Этот код не выполнится из-за ошибки
#
#     # raise Exception("Что-то пошло не так!")  # Искусственно создаём ошибку
#
# except Exception as e:
#     conn.rollback()  # Откатываем все изменения
#     print("Ошибка:", e)
#
# finally:
#     conn.close()  # Закрываем соединение

# import sqlite3
#
# # Подключение к базе
# conn = sqlite3.connect("mydb.db")
# cursor = conn.cursor()
#
# # Выполняем запрос
# cursor.execute("SELECT * FROM users")
#
# math_students = cursor.fetchall()
#
# # Получаем одну строку
# # row = cursor.fetchone()
# rows = cursor.fetchmany(5)
# # rows = cursor.fetchall()
# print(rows)  # Выведет, например: (1, 'Алиса', 25)
#
# conn.close()
#
# if not conn:
#     print("Соединение с базой данных закрыто.")
#     raise Exception()
# cursor.execute("SELECT * FROM users")

import sqlite3

# Подключение к базе данных (если файла нет, он будет создан)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создание таблицы users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL
);
''')

# Сохранение изменений
conn.commit()
# conn.close()

# Добавление данных
cursor.executemany('''
INSERT INTO users (name, age, email) VALUES (?, ?, ?)
''', [
    ('Иван Иванов', 28, 'ivan@example.com'),
    ('Мария Смирнова', 34, 'maria@example.com'),
    ('Петр Петров', 22, 'peter@example.com'),
    ('Алексей Иванов', 25, 'alexey@example.com'),
    ('Ольга Сидорова', 29, 'olga@example.com')
])

# Сохранение изменений
conn.commit()
# conn.close()
# Выполнение запроса
cursor.execute('SELECT * FROM users')

# Получение всех строк
users = cursor.fetchall()

# Вывод данных
for user in users:
    print(user)

# conn.close()
# Выполнение запроса с фильтрацией
cursor.execute('SELECT name, age, email FROM users WHERE age > ?', (25,))

# Получение и вывод данных
filtered_users = cursor.fetchall()
for user in filtered_users:
    print(user)
conn.close()