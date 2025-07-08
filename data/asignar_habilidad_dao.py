"""
1   Data Access Object for asignar_habilidad table(s)
"""

def get_all(conn):
    cursor = conn.execute("SELECT * FROM AsignarHabilidad;")
    return cursor.fetchall()

def get_by_id(conn, id_):
    cursor = conn.execute("SELECT * FROM AsignarHabilidad WHERE id_asignar_habilidad= ?;", (id_,))
    return cursor.fetchone()

def insert(conn, data_dict):
    keys = ", ".join(data_dict.keys())
    placeholders = ", ".join("?" for _ in data_dict)
    query = f"INSERT INTO AsignarHabilidad ({keys}) VALUES ({placeholders})"
    conn.execute(query, tuple(data_dict.values()))
    conn.commit()
