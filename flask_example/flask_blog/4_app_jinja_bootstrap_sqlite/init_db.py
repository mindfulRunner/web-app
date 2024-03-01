import sqlite3

connection = sqlite3.connect('database.db') # will create DB database.db when running this script

with open('db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()

print('Database "database.db" was created')
print('Table "posts" was created and filled')