"""
Data Access Object for equipamiento table(s)
"""

def get_all(conn):
    cursor = conn.execute("SELECT * FROM Equipamiento;")
    return cursor.fetchall()

def get_by_id(conn, id_):
    cursor = conn.execute("SELECT * FROM Equipamiento WHERE id_equipamiento= ?;", (id_,))
    return cursor.fetchone()

def insert(conn, data_dict):
    keys = ", ".join(data_dict.keys())
    placeholders = ", ".join("?" for _ in data_dict)
    query = f"INSERT INTO Equipamiento ({keys}) VALUES ({placeholders})"
    conn.execute(query, tuple(data_dict.values()))
    conn.commit()
