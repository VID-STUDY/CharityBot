from telegram.ext import CallbackQueryHandler, CallbackContext, ConversationHandler
from telegram import Update

from charity.models import TelegramUser, TelegramUserComplain, HelpRequest
from .resources import strings, keyboards
from bot.utils import Navigation


TEXT = range(1)

def give_away_offer_user_comlain(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.data.split(':')[1]
    try:
        user_to = TelegramUser.objects.get(pk=offer_id)
    except TelegramUser.DoesNotExist:
        query.answer()
        return
    user = TelegramUser.objects.get(pk=query.from_user.id)
    context.user_data['complain'] = {}
    context.user_data['complain']['user_to'] = user_to
    context.user_data['complain']['user_from'] = user
    complain_message = strings.get_string('give_away.complain.text', user.language)
    complain_keyboard = keyboards.get_keyboard('complain', user.language)
    query.message.reply_text(text=complain_message, reply_markup=complain_keyboard)
    return TEXT


def give_away_offer_user_complain_text(update: Update, context: CallbackContext):
    message = update.message
    complain_text = message.text
    complain = TelegramUserComplain.objects.create(text=complain_text, 
                                                   user_from=context.user_data['complain']['user_from'],
                                                   user_to=context.user_data['complain']['user_to'])
    complain_success = strings.get_string('complain.success', context.user_data['complain']['user_from'].language)
    Navigation.to_main_menu(update, context, message=complain_success)
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext):
    if 'complain' in context.user_data:
        del context.user_data['complain']
    Navigation.to_main_menu(update, context)
    return ConversationHandler.END
