import sqlite3

conn = sqlite3.connect("python_test")

cursor = conn.cursor()

cursor.execute("create table game(id varchar(20) primary key,name varchar(20))")

cursor.close()

conn.commit()

conn.close()