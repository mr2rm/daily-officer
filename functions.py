import sqlite3

from settings import DB_NAME


def get_db():
	db = sqlite3.connect(DB_NAME)
	cursor = db.cursor()
	return db, cursor
