"""
Business logic / service layer for raza
"""
import sqlite3
from data import raza_dao as dao

DB = "rpg.db"

def list_razas():
    with sqlite3.connect(DB) as conn:
        return dao.get_all(conn)
