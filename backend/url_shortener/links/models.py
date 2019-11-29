from django.db import models
from django.db.models.signals import post_save
import short_url


class Links(models.Model):
    original_url = models.CharField(max_length=300)
    short_url = models.CharField(max_length=30, blank=True)
    lifetime_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url


def create_short_url(sender, instance, **kwargs):
    if kwargs['created']:
        instance.short_url = short_url.encode_url(instance.id)
        instance.save()


post_save.connect(create_short_url, sender=Links)

# python manage.py makemigrations
# python manage.py migrate
