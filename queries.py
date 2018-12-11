GET_OR_CREATE_CHATS_TABLE = """
	CREATE TABLE IF NOT EXISTS chats(
		chat_id INTEGER UNIQUE NOT NULL,
		is_active BOOLEAN DEFAULT 1,
		created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
		last_modified_date DATETIME DEFAULT CURRENT_TIMESTAMP
	)
"""

INSERT_INTO_CHATS_TABLE = """
	INSERT INTO chats(chat_id)
	VALUES (?)
"""

GET_CHAT = """
	SELECT *
	FROM chats
	WHERE chat_id = ?
"""

GET_ACTIVE_CHATS = """
	SELECT *
	FROM chats
	WHERE is_active = 1
"""

UPDATE_CHAT_ID = """
	UPDATE chats
	SET
		chat_id = ?,
		last_modified_date = datetime('now')
	WHERE chat_id = ?
"""
