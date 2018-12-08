import sqlite3
import datetime
import math
import random

from settings import DB_NAME


def db_execute(query, *args, **kwargs):
	db = sqlite3.connect(DB_NAME)
	cursor = db.cursor()
	cursor.execute(query, args)
	if kwargs.get('fetch'):
		return cursor.fetchall()
	db.commit()
	db.close()


def is_admin(bot, message):
	chat = message.chat
	if chat.type == chat.PRIVATE:
		return True
	admin_users = [admin.user for admin in bot.get_chat_administrators(chat.id)]
	return message.from_user in admin_users


def get_random_time(start_time, end_time):
	def total_minute(this_time):
		return this_time.hour * 60 + this_time.minute

	def get_time(minutes):
		time_params = divmod(minutes, 60)
		return datetime.time(*time_params)

	if start_time > end_time:
		raise ValueError('start_time must be less than or equal to end_time')

	random_minutes = random.randint(total_minute(start_time), total_minute(end_time))
	return get_time(random_minutes)


def get_random_penalty(min_penalty, max_penalty):
	if min_penalty > max_penalty:
		raise ValueError('min_penalty must be less than or equal to max_penalty')

	min_penalty = 1000 * math.floor(min_penalty / 1000)
	max_penalty = 1000 * math.ceil(max_penalty / 1000)
	penalty_range = range(min_penalty, max_penalty + 1, 1000)

	return random.choice(penalty_range)
