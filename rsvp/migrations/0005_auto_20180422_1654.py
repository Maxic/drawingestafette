# Generated by Django 2.0.4 on 2018-04-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0004_auto_20180421_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='websiteAddress',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]