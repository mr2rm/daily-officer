GET_OR_CREATE_CHATS_TABLE = """
	CREATE TABLE IF NOT EXISTS chats(
		chat_id BIGINT UNIQUE NOT NULL,
		is_active BOOLEAN DEFAULT TRUE,
		created_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
		last_modified_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
	)
"""

GET_CHAT = """
	SELECT *
	FROM chats
	WHERE chat_id = %s
"""

INSERT_INTO_CHATS_TABLE = """
	INSERT INTO chats(chat_id)
	VALUES (%s)
"""

GET_ACTIVE_CHATS = """
	SELECT *
	FROM chats
	WHERE is_active = TRUE
"""

UPDATE_CHAT_ID = """
	UPDATE chats
	SET
		chat_id = %s,
		last_modified_date = NOW()
	WHERE chat_id = %s
"""
