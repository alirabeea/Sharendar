# Generated by Django 2.2 on 2020-08-08 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='contact',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact1',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact2',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact3',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact4',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
