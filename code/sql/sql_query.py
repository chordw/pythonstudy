import sqlite3


connnn = sqlite3.connect("python_test")

cursorQuery = connnn.cursor()

cursorQuery.execute("select * from game")

values = cursorQuery.fetchall()

print(values)

cursorQuery.close()

connnn.close()
