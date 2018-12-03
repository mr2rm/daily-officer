import logging

from telegram.ext import Updater

import handlers
from functions import get_db
from settings import TOKEN, HANDLER_SUFFIX, REQUEST_KWARGS


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


if __name__ == "__main__":
	init_db()
	setup_configs()

	updater, dispatcher, job_queue = get_bot()
	add_handlers(dispatcher)

	updater.start_polling()
	updater.idle()
