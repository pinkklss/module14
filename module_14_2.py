import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

users_data = [('User1', 'example1@gmail.com', 10, 1000),
              ('User2', 'example2@gmail.com', 20, 1000),
              ('User3', 'example3@gmail.com', 30, 1000),
              ('User4', 'example4@gmail.com', 40, 1000),
              ('User5', 'example5@gmail.com', 50, 1000),
              ('User6', 'example6@gmail.com', 60, 1000),
              ('User7', 'example7@gmail.com', 70, 1000),
              ('User8', 'example8@gmail.com', 80, 1000),
              ('User9', 'example9@gmail.com', 90, 1000),
              ('User10', 'example10@gmail.com', 100, 1000)]

cursor.execute('''DELETE FROM Users WHERE id in
(SELECT id FROM Users WHERE id%3 = 0)''')

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <> 60')
rows = cursor.fetchall()
for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')
total_records = cursor.fetchone()[0]
print(f'Общее количество записей: {total_records}')

cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(f'Сумма всех балансов: {total_balance}')

cursor.execute('SELECT AVG(balance) FROM Users')
average_balance = cursor.fetchone()[0]
print(f'Средний баланс всех пользователей: {average_balance}')

connection.commit()
connection.close()
