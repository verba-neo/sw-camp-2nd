# Generated by Django 4.2.2 on 2023-06-28 00:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stars',
            field=models.ManyToManyField(related_name='fans', to=settings.AUTH_USER_MODEL),
        ),
    ]
