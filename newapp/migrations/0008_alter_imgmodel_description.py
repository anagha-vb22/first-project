# Generated by Django 4.1.5 on 2023-02-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_rename_prize_wishlist_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgmodel',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
