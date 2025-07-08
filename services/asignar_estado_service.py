"""
Business logic / service layer for asignar_estado
"""
import sqlite3
from data import asignar_estado_dao as dao

DB = "rpg.db"

def list_asignar_estados():
    with sqlite3.connect(DB) as conn:
        return dao.get_all(conn)
