from django.db import models

class TelegramUser(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=2)


class HelpRequest(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.CharField(max_length=1024)
    help_type = models.CharField(max_length=20)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        get_latest_by = 'created_at'


class GiveAwayOffer(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    give_away_type = models.CharField(max_length=20)
    description = models.CharField(max_length=1024)
    photo_telegram_id = models.CharField(max_length=150, null=True, blank=True)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)


class TelegramUserComplain(models.Model):
    text = models.CharField(max_length=500)
    user_from = models.ForeignKey(TelegramUser, on_delete=models.SET_NULL, blank=True, null=True)
    user_to = models.ForeignKey(TelegramUser, on_delete=models.SET_NULL, blank=True, null=True)
