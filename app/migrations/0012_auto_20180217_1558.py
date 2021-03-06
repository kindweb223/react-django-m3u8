# Generated by Django 2.0.2 on 2018-02-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180113_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='Hide from public playlist'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='path',
            field=models.CharField(max_length=1024, verbose_name='Path to content'),
        ),
    ]
