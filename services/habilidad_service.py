"""
Business logic / service layer for habilidad
"""
import sqlite3
from data import habilidad_dao as dao

DB = "rpg.db"

def list_habilidads():
    with sqlite3.connect(DB) as conn:
        return dao.get_all(conn)
