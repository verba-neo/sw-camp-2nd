# Generated by Django 4.2.2 on 2023-06-20 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='THIS IS DEFAULT CONTENT'),
        ),
    ]
