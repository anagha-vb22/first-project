# Generated by Django 4.1.5 on 2023-02-20 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0011_buy_customercard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='imgfile',
        ),
    ]
