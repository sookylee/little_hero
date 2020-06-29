from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    address_city = models.CharField(max_length=100)
    address_gu = models.CharField(max_length=100)
    address_remainder = models.CharField(max_length=200, default='')
    recruit_status = models.BooleanField(default=True)
    adult_status = models.NullBooleanField() #if null then both adult and student
    domain = models.TextField(default='')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    end_date = models.DateTimeField(
            blank=True, null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title