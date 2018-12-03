import logging
import sqlite3

from telegram.ext import Updater

import handlers
from local_settings import TOKEN
from settings import DB_NAME, HANDLER_SUFFIX, REQUEST_KWARGS


def get_db():
	db = sqlite3.connect(DB_NAME)
	cursor = db.cursor()
	return db, cursor


def init_db():
	chats_table_sql = """
		CREATE TABLE IF NOT EXISTS chats(
			chat_id TEXT UNIQUE NOT NULL
		)
	"""

	db, cursor = get_db()
	cursor.execute(chats_table_sql)
	db.commit()
	db.close()


def setup_configs():
	logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.INFO
	)


def get_bot():
	updater = Updater(token=TOKEN, request_kwargs=REQUEST_KWARGS)
	return updater, updater.dispatcher, updater.job_queue


def add_handlers(dispatcher):
	for name in dir(handlers):
		if name.endswith(HANDLER_SUFFIX):
			handler = getattr(handlers, name)
			dispatcher.add_handler(handler)
