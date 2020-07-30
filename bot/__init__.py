from telegram.ext import Updater

from bot import registration, needhelp

from os import getenv


updater = Updater(getenv('TELEGRAM_BOT_TOKEN'), use_context=True)
dp = updater.dispatcher

dp.add_handler(registration.registration_conversation_handler)
dp.add_handler(needhelp.help_request_conversation)
