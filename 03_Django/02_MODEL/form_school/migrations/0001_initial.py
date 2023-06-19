# Generated by Django 4.2.2 on 2023-06-19 01:15

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
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('age', models.PositiveSmallIntegerField()),
                ('major', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('bio', models.TextField()),
            ],
        ),
    ]
