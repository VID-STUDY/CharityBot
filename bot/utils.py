from bot.resources import strings, keyboards
from telegram.ext import BaseFilter


class Navigation:
    @staticmethod
    def to_main_menu(update, context, message=None):
        main_menu_message = strings.get_string('main_menu', context.user_data['user'].language)
        if message:
            main_menu_message = message
        main_menu_keyboard = keyboards.get_keyboard('main_menu', context.user_data['user'].language)
        update.message.reply_text(text=main_menu_message, reply_markup=main_menu_keyboard)


class CharityFilters:

    class NeedHelpFilter(BaseFilter):
        def filter(self, message):
            return message.text and ((strings.get_string('menu.need_help', 'ru') in message.text) or 
                                    (strings.get_string('menu.need_help', 'uz') in message.text))
    
    class CancelFilter(BaseFilter):
        def filter(self, message):
            return message.text and ((strings.get_string('cancel', 'ru') in message.text) or
                                    (strings.get_string('cancel', 'uz') in message.text))
