# Generated by Django 4.1.5 on 2023-02-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0008_alter_imgmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='description',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='imgmodel',
            name='description',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='description',
            field=models.CharField(max_length=600),
        ),
    ]
