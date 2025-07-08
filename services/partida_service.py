"""
Business logic / service layer for partida
"""
import sqlite3
from data import partida_dao as dao

DB = "rpg.db"

def list_partidas():
    with sqlite3.connect(DB) as conn:
        return dao.get_all(conn)
