import logging
import sqlite3

from telegram.ext import Updater

import handlers
from queries import GET_OR_CREATE_CHATS_TABLE
from local_settings import TOKEN
from settings import DB_NAME, HANDLER_SUFFIX, REQUEST_KWARGS


def db_execute(query, params=None):
	db = sqlite3.connect(DB_NAME)
	cursor = db.cursor()
	cursor.execute(query, params)
	db.commit()
	db.close()


def setup_configs():
	db_execute(GET_OR_CREATE_CHATS_TABLE)

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
