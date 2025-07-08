"""
logica de negocio / service layer for equipamiento
"""
import sqlite3
from data import equipamiento_dao as dao

DB = "rpg.db"

def list_equipamientos():
    with sqlite3.connect(DB) as conn:
        return dao.get_all(conn)
