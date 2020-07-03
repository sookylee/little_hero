# Generated by Django 3.0.7 on 2020-06-29 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address_remainder',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='recruit_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='address_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='address_gu',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
