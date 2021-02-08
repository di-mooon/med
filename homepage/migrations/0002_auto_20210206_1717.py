# Generated by Django 3.1.5 on 2021-02-06 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card_comments',
            name='name',
        ),
        migrations.AddField(
            model_name='card_comments',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='User'),
            preserve_default=False,
        ),
    ]
