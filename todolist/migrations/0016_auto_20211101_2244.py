# Generated by Django 3.2.8 on 2021-11-01 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0015_alter_testmodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceukModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]