import datetime
import logging

from telegram.ext import Updater

import handlers
from functions import db_execute
from local_settings import TOKEN
from queries import GET_OR_CREATE_CHATS_TABLE
from settings import REQUEST_KWARGS, HANDLER_SUFFIX
from tasks import send_daily_message


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


if __name__ == "__main__":
	setup_configs()

	updater, dispatcher, job_queue = get_bot()
	add_handlers(dispatcher)

	job_queue.run_daily(send_daily_message, datetime.time())

	updater.start_polling()
	updater.idle()
