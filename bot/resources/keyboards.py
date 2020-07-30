from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from .strings import get_string
from typing import Union, Optional


def _create_keyboard(keyboard: list, one_time: bool = False) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=one_time)


def get_keyboard(key, language='ru') -> Union[ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup]:
    if key == 'start.languages':
        return _create_keyboard([[get_string('languages.ru', language), get_string('languages.uz', language)]])
    elif key == 'start.phone':
        keyboard = [[KeyboardButton(get_string('phone', language), request_contact=True)]]
        return _create_keyboard(keyboard)
    elif key == 'main_menu':
        keyboard = [
            [get_string('menu.need_help', language), get_string('menu.can_help', language)],
            [get_string('menu.give_away', language)],
            [get_string('menu.share', language)],
            [get_string('menu.chage_language', language)]
        ]
        return _create_keyboard(keyboard)
    elif key == 'remove':
        return ReplyKeyboardRemove()
    elif key == 'need_help.type':
        keyboard = [
            [get_string('products', language), get_string('medicines', language)],
            [get_string('cancel', language)]
        ]
        return _create_keyboard(keyboard)
    elif key == 'need_help.description':
        keyboard = [[get_string('cancel', language)]]
        return _create_keyboard(keyboard)
    elif key == 'need_help.location':
        keyboard = [
            [KeyboardButton(get_string('location', language), request_location=True)],
            [get_string('cancel', language)]
        ]
        return _create_keyboard(keyboard)
    else:
        return _create_keyboard([['no_keyboard']])