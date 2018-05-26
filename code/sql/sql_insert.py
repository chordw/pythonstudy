import sqlite3

conn = sqlite3.connect("python_test")

cursor = conn.cursor()

cursor.execute("insert into game(name) values('仙剑奇侠传')")

cursor.close()

conn.close()