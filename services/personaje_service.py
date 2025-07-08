"""
Business logic / service layer for personaje
"""
import sqlite3
from data import personaje_dao as dao

DB = "rpg.db"

def list_personajes():
    with sqlite3.connect(DB) as conn:
        return dao.get_all(conn)
