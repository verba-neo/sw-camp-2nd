# Generated by Django 4.2.2 on 2023-06-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mbti',
            field=models.CharField(choices=[(1, 'ESTP'), (2, 'ESTJ'), (3, 'ESFP'), (4, 'ESFJ')], max_length=4),
        ),
    ]