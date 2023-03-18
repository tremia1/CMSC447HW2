import sqlite3
from users import Users

connection = sqlite3.connect('users.db')

curso = connection.cursor()
curso.execute("""DROP TABLE IF EXISTS users""")
curso.execute("""CREATE TABLE users(user_id int NOT NULL PRIMARY KEY,first_name text NOT NULL,last_name text NOT NULL,points int NOT NULL)""")




curso.execute("INSERT INTO users (user_id, first_name, last_name, points) VALUES (?,?,?,?)",
              (211, 'Steve', 'Smith', 80))

curso.execute("INSERT INTO users (user_id, first_name, last_name, points) VALUES (?,?,?,?)",
              (122, 'Jian', 'Wong', 92))

curso.execute("INSERT INTO users (user_id, first_name, last_name, points) VALUES (?,?,?,?)",
              (213, 'Chris', 'Peterson', 91))

curso.execute("INSERT INTO users (user_id, first_name, last_name, points) VALUES (?,?,?,?)",
              (524, 'Sai', 'Patel', 94))

curso.execute("INSERT INTO users (user_id, first_name, last_name, points) VALUES (?,?,?,?)",
              (425, 'Andrew', 'Whitehead', 99))

curso.execute("INSERT INTO users (user_id, first_name, last_name, points) VALUES (?,?,?,?)",
              (626, 'Lynn', 'Roberts', 90))

curso.execute("INSERT INTO users (user_id, first_name, last_name, points) VALUES (?,?,?,?)",
              (287, 'Robert', 'Sanders', 75))
connection.commit()
connection.close()