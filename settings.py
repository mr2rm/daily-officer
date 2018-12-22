# General Settings
HANDLER_SUFFIX = 'handler'

# Request Configuration
REQUEST_KWARGS = {}

try:
	from local_settings import *
except ImportError:
	pass
