# General Settings
HANDLER_SUFFIX = 'handler'

# Request Configuration
REQUEST_KWARGS = {}

# Database Settings
DB_NAME = 'db.sqlite3'

try:
	from local_settings import *
except ImportError:
	pass
