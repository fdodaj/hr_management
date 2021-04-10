from django.db import models


class Holiday(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date = models.DateField()
    date_created = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.name

