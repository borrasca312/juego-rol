"""
Data Access Object for personaje table(s)
"""

def get_all(conn):
    cursor = conn.execute("SELECT * FROM Personaje;")
    return cursor.fetchall()

def get_by_id(conn, id_):
    cursor = conn.execute("SELECT * FROM Personaje WHERE id_personaje= ?;", (id_,))
    return cursor.fetchone()

def insert(conn, data_dict):
    keys = ", ".join(data_dict.keys())
    placeholders = ", ".join("?" for _ in data_dict)
    query = f"INSERT INTO Personaje ({keys}) VALUES ({placeholders})"
    conn.execute(query, tuple(data_dict.values()))
    conn.commit()
