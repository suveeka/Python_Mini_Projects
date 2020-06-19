import sqlite3

db = sqlite3.connect('Login.db')

cur = db.cursor()

# Comment this line if running for the first time or an exception will occur
cur.execute("DROP TABLE users")

cur.execute("CREATE TABLE users(username TEXT,password TEXT)")

cur.execute("INSERT INTO users VALUES (?,?)",("harry","potter"))

cur.execute("INSERT INTO users VALUES (?,?)",("tom","cat"))

cur.execute("INSERT INTO users VALUES (?,?)",("jon","snow"))

cur.execute("SELECT * FROM users")

users = {}

[users.update({row[0]:row[1]}) for row in cur]

db.commit()

db.close()