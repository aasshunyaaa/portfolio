# Generated by Django 3.0.7 on 2020-06-23 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site2', '0005_auto_20200623_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('discription', models.TextField(max_length=500, verbose_name='説明')),
                ('public_status', models.BooleanField(default=False, verbose_name='公開・非公開')),
                ('long_short', models.BooleanField(verbose_name='長期/短期')),
            ],
        ),
        migrations.DeleteModel(
            name='RecruitLong',
        ),
        migrations.DeleteModel(
            name='RecruitShort',
        ),
    ]