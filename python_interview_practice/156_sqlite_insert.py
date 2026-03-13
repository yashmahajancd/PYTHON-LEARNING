import sqlite3
conn=sqlite3.connect("db.db")
conn.execute("INSERT INTO users VALUES(1,'A')")
conn.commit()
conn.close()