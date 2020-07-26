from telegram.ext import Updater

from os import getenv


updater = Updater(getenv('TELEGRAM_BOT_TOKEN'), use_context=True)
dp = updater.dispatcher
