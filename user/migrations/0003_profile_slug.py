# Generated by Django 3.1.5 on 2021-02-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210205_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='', verbose_name='URL'),
            preserve_default=False,
        ),
    ]
