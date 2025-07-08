"""
Data Access Object for asignar_estado table(s)
"""

def get_all(conn):
    cursor = conn.execute("SELECT * FROM AsignarEstado;")
    return cursor.fetchall()

def get_by_id(conn, id_):
    cursor = conn.execute("SELECT * FROM AsignarEstado WHERE id_asignar_estado= ?;", (id_,))
    return cursor.fetchone()

def insert(conn, data_dict):
    keys = ", ".join(data_dict.keys())
    placeholders = ", ".join("?" for _ in data_dict)
    query = f"INSERT INTO AsignarEstado ({keys}) VALUES ({placeholders})"
    conn.execute(query, tuple(data_dict.values()))
    conn.commit()
