# Generated by Django 2.2 on 2020-07-31 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_events_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]