# Generated by Django 3.2.8 on 2021-11-01 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0017_auto_20211101_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bitcoinprices',
            old_name='price',
            new_name='priceuk',
        ),
    ]