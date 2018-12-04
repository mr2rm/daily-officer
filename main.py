from functions import add_handlers, get_bot, setup_configs

if __name__ == "__main__":
	setup_configs()

	updater, dispatcher, job_queue = get_bot()
	add_handlers(dispatcher)

	updater.start_polling()
	updater.idle()
