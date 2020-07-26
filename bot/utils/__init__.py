from bot.resources import strings, keyboards


class Navigation:
    @staticmethod
    def to_main_menu(update, context):
        main_menu_message = strings.get_string('main_menu', context.user_data['user'].language)
        main_menu_keyboard = keyboards.get_keyboard('main_menu', context.user_data['user'].language)
        update.message.reply_text(text=main_menu_message, reply_markup=main_menu_keyboard)