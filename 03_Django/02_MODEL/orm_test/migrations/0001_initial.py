# Generated by Django 4.2.2 on 2023-06-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('major', models.CharField(max_length=100)),
                ('mbti', models.CharField(max_length=4)),
            ],
        ),
    ]
