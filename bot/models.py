from django.db import models


class TgUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name