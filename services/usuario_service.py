"""
Business logic / service layer for usuario
"""
import sqlite3
from data import usuario_dao as dao

DB = "rpg.db"

def list_usuarios():
    with sqlite3.connect(DB) as conn:
        return dao.get_all(conn)
