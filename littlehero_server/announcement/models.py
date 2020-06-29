from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    regist_no = models.BigIntegerField(default=0)
    author = models.CharField(default='', max_length=200)
    title = models.CharField(max_length=300)
    address_city = models.CharField(max_length=100, default='')
    address_gu = models.CharField(max_length=100, default='')
    address_remainder = models.CharField(max_length=200, default='')
    recruit_status = models.BooleanField(default=True)
    adult_status = models.CharField(default='', max_length=200) #if null then both adult and student
    domain = models.TextField(default='')
    telephone = models.CharField(max_length=200, default='')
    text = models.TextField(default='')
    do_date = models.CharField(default='', max_length=200)
    do_time = models.CharField(default='', max_length=200)
    do_week = models.CharField(default='', max_length=200)
    recruit_date = models.CharField(default='', max_length=200)
    recruit_company = models.CharField(default='', max_length=300)
    recruit_member = models.CharField(default='0 명 / 일', max_length=200)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title