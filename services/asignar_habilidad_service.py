"""
Business logic / service layer for asignar_habilidad
"""
import sqlite3
from data import asignar_habilidad_dao as dao

DB = "rpg.db"

def list_asignar_habilidads():
    with sqlite3.connect(DB) as conn:
        return dao.get_all(conn)
