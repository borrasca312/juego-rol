"""
Business logic / service layer for estado_personalizado
"""
import sqlite3
from data import estado_personalizado_dao as dao

DB = "rpg.db"

def list_estado_personalizados():
    with sqlite3.connect(DB) as conn:
        return dao.get_all(conn)
