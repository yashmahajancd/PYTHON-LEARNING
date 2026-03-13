import sqlite3
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
print(conn.execute("SELECT * FROM users").fetchall())
conn.execute("INSERT INTO users (name) VALUES ('Alice')")
print(conn.execute("SELECT * FROM users").fetchall())
conn.execute("INSERT INTO users (name) VALUES ('Bob')")
print(conn.execute("SELECT * FROM users").fetchall())
conn.close()