# Generated by Django 3.0.7 on 2020-07-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site2', '0009_auto_20200701_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='data',
            field=models.DateField(auto_now=True, verbose_name='更新日時'),
        ),
    ]
