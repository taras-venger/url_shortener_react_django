from django.db import models


class Links(models.Model):
    original_url = models.URLField()
    lifetime_days = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.original_url
