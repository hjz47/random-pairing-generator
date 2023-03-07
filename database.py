import sqlite3


"""
List all information in table
"""
def list_all():

    conn = sqlite3.connect("data.db")
    cur = conn.cursor()

    val = None

    try:
        cur.execute(
            """
            SELECT * 
            FROM Data
            """
        )

        val = cur.fetchall()

    except Exception as e:
        print("Sorry, we caught this exception:", e)

    cur.close()
    conn.close()
    
    return val

"""
Add a name to the database
"""
def add_character(name, fandom, media):

    name = name.strip()
    fandom = fandom.strip()
    media = media.strip()

    conn = sqlite3.connect("data.db")
    cur = conn.cursor()

    val = None
    
    try:
        sql = """
              INSERT INTO Data
              VALUES (?, ?, ?)
              """
        cur.execute(sql, (name, fandom, media))

        conn.commit()

    except Exception as e:
        print("Sorry, we caught this exception:", e)

    cur.close()
    conn.close()

    return val

"""
Retrieve a random name from the database
"""
def get_random():

    conn = sqlite3.connect("data.db")
    cur = conn.cursor()

    val = None

    try:
        cur.execute(
            """
            SELECT * FROM Data
            ORDER BY RANDOM()
            LIMIT 1
            """
        )

        val = cur.fetchall()

    except Exception as e:
        print("Sorry, we caught this exception:", e)

    cur.close()
    conn.close()

    return val
