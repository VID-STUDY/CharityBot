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
