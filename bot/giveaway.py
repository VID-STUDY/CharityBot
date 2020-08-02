from telegram.ext import ConversationHandler, MessageHandler, Filters
from telegram import ParseMode

from bot.utils import Navigation, Geolocation, CharityFilters
from charity.models import TelegramUser, GiveAwayOffer
from .resources import strings, keyboards


ACTION, TYPE, DESCRIPTION, IMAGE, GIVE_LOCATION, GET_LOCATION = range(6)


def give_away(update, context):
    message = update.message
    if 'user' not in context.user_data:
        try:
            user = TelegramUser.objects.get(pk=message.from_user.id)
        except TelegramUser.DoesNotExist:
            return ConversationHandler.END
        context.user_data['user'] = user
    language = context.user_data['user'].language
    start_message = strings.get_string('give_away.start', language)
    start_keyboard = keyboards.get_keyboard('give_away.start', language)
    message.reply_text(text=start_message, reply_markup=start_keyboard)
    return ACTION


def give_away_action(update, context):
    message = update.message
    language = context.user_data['user'].language
    if strings.get_string('give_away.give', language) in message.text:
        reply_message = strings.get_string('give_away.type', language)
        reply_keyboard = keyboards.get_keyboard('give_away.type', language)
        NEXT_STEP = TYPE
    elif strings.get_string('give_away.get', language) in message.text:
        reply_message = strings.get_string('give_away.get_location', language)
        reply_keyboard = keyboards.get_keyboard('give_away.get_location', language)
        NEXT_STEP = GET_LOCATION
    else:
        start_message = strings.get_string('give_away.start', language)
        start_keyboard = keyboards.get_keyboard('give_away.start', language)
        message.reply_text(text=start_message, reply_markup=start_keyboard)
        return ACTION
    message.reply_text(text=reply_message, reply_markup=reply_keyboard)
    return NEXT_STEP


def give_away_type(update, context):
    message = update.message
    language = context.user_data['user'].language
    context.user_data['give_away_offer'] = {}
    context.user_data['give_away_offer']['type'] = message.text
    description_message = strings.get_string('give_away.description', language)
    description_keyboard = keyboards.get_keyboard('give_away.description', language)
    message.reply_text(text=description_message, reply_markup=description_keyboard)
    return DESCRIPTION


def give_away_description(update, context):
    message = update.message
    language = context.user_data['user'].language
    context.user_data['give_away_offer']['description'] = message.text
    image_message = strings.get_string('give_away.image', language)
    image_keyboard = keyboards.get_keyboard('give_away.image', language)
    message.reply_text(text=image_message, reply_markup=image_keyboard)
    return IMAGE


def give_away_image(update, context):
    message = update.message
    language = context.user_data['user'].language
    photo = message.photo[-1]
    context.user_data['give_away_offer']['photo_telegram_id'] = photo.file_id
    give_location_message = strings.get_string('give_away.give_location', language)
    give_location_keyboard = keyboards.get_keyboard('give_away.give_location', language)
    message.reply_text(text=give_location_message, reply_markup=give_location_keyboard)
    return GIVE_LOCATION


def give_away_give_location(update, context):
    message = update.message
    latitude = message.location.latitude
    longitude = message.location.longitude
    language = context.user_data['user'].language
    GiveAwayOffer.objects.create(latitude=latitude, longitude=longitude,
                                description=context.user_data['give_away_offer']['description'],
                                user=context.user_data['user'],
                                give_away_type=context.user_data['give_away_offer']['type'],
                                photo_telegram_id=context.user_data['give_away_offer']['photo_telegram_id'])
    del context.user_data['give_away_offer']
    success_message = strings.get_string('give_away.success', language)
    Navigation.to_main_menu(update, context, message=success_message)
    return ConversationHandler.END


def give_away_get_location(update, context):
    message = update.message
    latitude = message.location.latitude
    longitude = message.location.longitude
    give_away_offers = GiveAwayOffer.objects.all()
    results = []
    for offer in give_away_offers:
        distance = Geolocation.distance_between_two_points((latitude, longitude), (offer.latitude, offer.longitude))
        if distance <= 1:
            results.append({
                'distance': distance,
                'offer': offer
            })
    language = context.user_data['user'].language
    if not results:
        empty_message = strings.get_string('give_away.empty', language)
        Navigation.to_main_menu(update, context, message=empty_message)
        return ConversationHandler.END
    results = sorted(results, key=lambda i: i['distance'])
    exists_message = strings.get_string('give_away.exists', language)
    Navigation.to_main_menu(update, context, message=exists_message)
    for result in results:
        offer_message = strings.from_give_away_offer_distance(result, language)
        offer_keyboard = keyboards.from_give_away_offer_keybaord(result['offer'], language)
        message.reply_photo(photo=result['offer'].photo_telegram_id, caption=offer_message, 
                            reply_markup=offer_keyboard, parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def cancel(update, context):
    if 'give_away_offer' in context.user_data:
        del context.user_data['give_away_offer']
    Navigation.to_main_menu(update, context)
    return ConversationHandler.END


give_away_conversation = ConversationHandler(
    entry_points=[MessageHandler(CharityFilters.GiveAwayFiler(), give_away)],
    states={
        ACTION: [MessageHandler(CharityFilters.CancelFilter(), cancel), MessageHandler(Filters.text, give_away_action)],
        TYPE: [MessageHandler(CharityFilters.CancelFilter(), cancel), MessageHandler(Filters.text, give_away_type)],
        DESCRIPTION: [MessageHandler(CharityFilters.CancelFilter(), cancel), MessageHandler(Filters.text, give_away_description)],
        IMAGE: [MessageHandler(CharityFilters.CancelFilter(), cancel), MessageHandler(Filters.photo, give_away_image)],
        GIVE_LOCATION: [MessageHandler(CharityFilters.CancelFilter(), cancel), MessageHandler(Filters.location, give_away_give_location)],
        GET_LOCATION: [MessageHandler(CharityFilters.CancelFilter(), cancel), MessageHandler(Filters.location, give_away_get_location)]
    },
    fallbacks=[MessageHandler(CharityFilters.CancelFilter(), cancel)]
)
