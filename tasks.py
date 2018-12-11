import datetime

from telegram.error import ChatMigrated, BadRequest

from functions import db_execute, get_random_time, get_random_penalty
from queries import GET_ACTIVE_CHATS, UPDATE_CHAT_ID


def send_daily_message(bot, job):
	today = datetime.date.today()
	if 3 <= today.weekday() <= 4:
		return

	active_chats = db_execute(GET_ACTIVE_CHATS, fetch=True)
	start_time, end_time = datetime.time(hour=9, minute=30), datetime.time(hour=11, minute=30)
	min_penalty, max_penalty = 0, 7000
	template_text = 'Time: {time}\nPenalty: {penalty}'

	for chat in active_chats:
		chat_id = chat[0]
		random_time = get_random_time(start_time, end_time)
		random_penalty = get_random_penalty(min_penalty, max_penalty)
		text = template_text.format(time=random_time.strftime('%H:%M'), penalty=random_penalty)

		try:
			message = bot.send_message(chat_id=chat_id, text=text)
		except ChatMigrated as error:
			db_execute(UPDATE_CHAT_ID, error.new_chat_id, chat_id)
			chat_id = error.new_chat_id
			message = bot.send_message(chat_id=chat_id, text=text)

		try:
			bot.pin_chat_message(chat_id, message.message_id)
		except BadRequest:
			pass
