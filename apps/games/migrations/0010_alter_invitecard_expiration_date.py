# Generated by Django 4.2.3 on 2023-07-21 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_rename_imgor_game_main_imgor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 20, 20, 23, 2, 357081), verbose_name='дата истечения'),
        ),
    ]