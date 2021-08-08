import sqlite3

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute ("""
    DROP TABLE IF EXISTS books

""")
cursor.execute("""
    CREATE TABLE (
        id integer PRIMARY KEY,
        title TEXT,
        pages INTEGER,
        current_page INTEGER
    )
""")

cursor.execute ("""
    INSERT INTO books VALUES (
        0, 'A great book',213,27
    )

""")

cursor.execute ("""
    INSERT INTO books VALUES (
        1, 'A great book',395,27
    )

""")

rows = cursor.execute("""
    SELECT title FROM books
"""

)



connection.commit()

connection.close()