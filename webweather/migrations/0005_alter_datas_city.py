# Generated by Django 3.2.8 on 2022-03-17 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webweather', '0004_alter_datas_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='city',
            field=models.CharField(max_length=200),
        ),
    ]
