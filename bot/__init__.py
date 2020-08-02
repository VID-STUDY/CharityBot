from telegram.ext import Updater

from bot import registration, needhelp, canhelp, giveaway, complains

from os import getenv


updater = Updater(getenv('TELEGRAM_BOT_TOKEN'), use_context=True)
dp = updater.dispatcher

dp.add_handler(registration.registration_conversation_handler)
dp.add_handler(needhelp.help_request_conversation)
dp.add_handler(canhelp.can_help_conversation)
dp.add_handler(giveaway.give_away_conversation)
dp.add_handler(giveaway.get_it_for_free_handler)
dp.add_handler(giveaway.give_it_away_handler)
dp.add_handler(complains.telegram_user_complain_conversation)
dp.add_handler(complains.help_request_complain_conversation)
