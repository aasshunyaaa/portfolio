# Generated by Django 3.0.7 on 2020-07-01 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site2', '0008_auto_20200625_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='public_status',
            field=models.BooleanField(verbose_name='公開'),
        ),
    ]
