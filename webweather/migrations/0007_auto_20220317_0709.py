# Generated by Django 3.2.8 on 2022-03-17 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webweather', '0006_alter_datas_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='datas',
            name='lat',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='datas',
            name='lon',
            field=models.FloatField(max_length=10, null=True),
        ),
    ]
