from telegram.ext import CommandHandler, MessageHandler, Filters


def say_hello(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Hello')


def set_timespan(bot, update):
	pass


def set_penalty(bot, update):
	pass


def unknown_command(bot, update):
	pass


start_handler = CommandHandler('start', say_hello)
timespan_handler = CommandHandler('timespan', set_timespan, pass_args=True)
penalty_handler = CommandHandler('penalty', set_penalty, pass_args=True)
unknown_handler = MessageHandler(Filters.command, unknown_command)
