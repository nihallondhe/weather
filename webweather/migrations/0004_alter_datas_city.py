# Generated by Django 3.2.8 on 2022-03-17 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webweather', '0003_alter_datas_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='city',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
