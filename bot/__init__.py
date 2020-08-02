from telegram.ext import Updater

from bot import registration, needhelp, canhelp, giveaway

from os import getenv


updater = Updater(getenv('TELEGRAM_BOT_TOKEN'), use_context=True)
dp = updater.dispatcher

dp.add_handler(registration.registration_conversation_handler)
dp.add_handler(needhelp.help_request_conversation)
dp.add_handler(canhelp.can_help_conversation)
dp.add_handler(giveaway.give_away_conversation)
