# Generated by Django 2.0.4 on 2018-04-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0005_auto_20180422_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='artwork1Price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork1SizeH',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork1SizeW',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork1Title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork2Price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork2SizeH',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork2SizeW',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork2Title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork3Price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork3SizeH',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork3SizeW',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='artwork3Title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='role',
            field=models.CharField(choices=[('Bachelorstudent', 'Bachelorstudent'), ('Masterstudent', 'Masterstudent'), ('Alumnus', 'Alumnus'), ('Other', 'Other')], default='Alumnus', max_length=20),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='websiteAddress',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
