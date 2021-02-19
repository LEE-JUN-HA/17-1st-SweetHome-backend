# Generated by Django 3.1.6 on 2021-02-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('posting', '0003_auto_20210218_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='like_user',
            field=models.ManyToManyField(related_name='user_like_posting', through='posting.PostingLike', to='user.User'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='scrap_user',
            field=models.ManyToManyField(related_name='user_scrap_posting', through='posting.PostingScrap', to='user.User'),
        ),
    ]
