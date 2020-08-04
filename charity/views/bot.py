from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from os import getenv


class StartBotView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        from bot import updater
        updater.start_webhook(listen='127.0.0.1', port=getenv('WEBHOOK_PORT'), url_path=getenv('TELEGRAM_BOT_TOKEN'))
        updater.bot.set_webhook(url='https://{host}/{path}'.format(host=getenv('WEBHOOK_HOST'), path=getenv('TELEGRAM_BOT_TOKEN')))
        return HttpResponse('Bot started!')