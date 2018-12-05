GET_OR_CREATE_CHATS_TABLE = """
	CREATE TABLE IF NOT EXISTS chats(
		chat_id INTEGER UNIQUE NOT NULL
	)
"""

INSERT_INTO_CHATS_TABLE = """
	INSERT INTO chats(chat_id)
	VALUES (?)
"""

GET_CHAT = """
	SELECT * FROM chats
	WHERE chat_id = (?)
"""
