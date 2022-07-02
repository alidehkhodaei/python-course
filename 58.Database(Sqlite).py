import sqlite3

#Example 1------------------

connection = sqlite3.connect("./my-database.db")
cursor = connection.cursor()
sql = """
CREATE TABLE IF NOT EXISTS user(
     user_id INTEGER,
     name VARCHAR(60),
     family VARCHAR(60),
     email VARCHAR(60)
    );
"""

cursor.execute(sql)
connection.commit() # Save (commit) the changes
connection.close()

#Example 2------------------

connection = sqlite3.connect("./my-database.db")
cursor = connection.cursor()

sql = """
INSERT INTO user VALUES(1,"Ali","Ahmadi","test@gmail.com")
"""

cursor.execute(sql)
connection.commit()
connection.close()

#Example 3------------------

connection = sqlite3.connect("./my-database.db")
cursor = connection.cursor()

sql = """
INSERT INTO user VALUES(2,"Mohammad","Jamali","test2@gmail.com");
INSERT INTO user VALUES(3,"Reza","Movahed","test3@gmail.com");
"""

cursor.executescript(sql) # Execute some query.
connection.commit()
connection.close()

#Example 4------------------

connection = sqlite3.connect("./my-database.db")
cursor = connection.cursor()

sql = """
 SELECT * FROM user 
"""
cursor.execute(sql)

for user in cursor:
    print(user)

'''
(1, 'Ali', 'Ahmadi', 'test@gmail.com')
(2, 'Mohammad', 'Jamali', 'test2@gmail.com')
(3, 'Reza', 'Movahed', 'test3@gmail.com')
'''

#connection.commit() We don't have this for select query if I do not modify the database (i.e. only do a SELECT query
connection.close()

#Example 5------------------

connection = sqlite3.connect("./my-database.db")
cursor = connection.cursor()

sql = """
 UPDATE user SET name="Vahid" WHERE user_id=2
"""
cursor.execute(sql)
connection.commit()
connection.close()

#Example 6------------------

connection = sqlite3.connect("./my-database.db")
cursor = connection.cursor()

sql = """
 DELETE FROM user 
"""
cursor.execute(sql)
connection.commit()
connection.close()
