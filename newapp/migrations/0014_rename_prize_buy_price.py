# Generated by Django 4.1.5 on 2023-02-20 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0013_rename_price_buy_prize'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='prize',
            new_name='price',
        ),
    ]
