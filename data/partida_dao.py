"""
Data Access Object for partida table(s)
"""

def get_all(conn):
    cursor = conn.execute("SELECT * FROM Partida;")
    return cursor.fetchall()

def get_by_id(conn, id_):
    cursor = conn.execute("SELECT * FROM Partida WHERE id_partida= ?;", (id_,))
    return cursor.fetchone()

def insert(conn, data_dict):
    keys = ", ".join(data_dict.keys())
    placeholders = ", ".join("?" for _ in data_dict)
    query = f"INSERT INTO Partida ({keys}) VALUES ({placeholders})"
    conn.execute(query, tuple(data_dict.values()))
    conn.commit()
