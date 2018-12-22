from telegram.ext import CommandHandler, MessageHandler, Filters

from functions import db_execute, is_admin
from queries.postgresql import INSERT_INTO_CHATS_TABLE, GET_CHAT


def save_chat(bot, update):
	message = update.message
	chat_id = message.chat_id
	text = 'Permission Denied'

	if is_admin(bot, message):
		chats = db_execute(GET_CHAT, chat_id, fetch=True)
		text = 'Already Started'

		if not chats:
			text = 'OK'
			db_execute(INSERT_INTO_CHATS_TABLE, chat_id)

	bot.send_message(chat_id=chat_id, text=text)


def set_timespan(bot, update):
	pass


def set_penalty(bot, update):
	pass


def unknown_command(bot, update):
	pass


start_handler = CommandHandler('start', save_chat)
timespan_handler = CommandHandler('timespan', set_timespan, pass_args=True)
penalty_handler = CommandHandler('penalty', set_penalty, pass_args=True)
unknown_handler = MessageHandler(Filters.command, unknown_command)
