import mysql.connector

conn = mysql.connector.connect(user="root",password="1992",database="java_test")

cursor = conn.cursor()

cursor.execute("select * from game")

values = cursor.fetchall()

print(values)

cursor.close()

conn.close()