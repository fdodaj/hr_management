from django.db import models


class Holiday(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()
    date_created = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
