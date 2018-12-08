import datetime

from functions import db_execute, get_random_time, get_random_penalty
from queries import GET_ACTIVE_CHATS


def send_daily_message(bot, job):
	active_chats = db_execute(GET_ACTIVE_CHATS, fetch=True)
	start_time, end_time = datetime.time(hour=9), datetime.time(hour=11)
	min_penalty, max_penalty = 0, 7000
	template_text = 'Time: {time}\nPenalty: {penalty}'

	for chat in active_chats:
		chat_id = chat[0]
		random_time = get_random_time(start_time, end_time)
		random_penalty = get_random_penalty(min_penalty, max_penalty)

		bot.send_message(chat_id=chat_id, text=template_text.format(
			time=random_time.strftime('%H:%M'),
			penalty=random_penalty,
		))
