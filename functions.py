import sqlite3

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
