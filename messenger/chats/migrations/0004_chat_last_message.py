# Generated by Django 4.1.2 on 2022-12-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_message_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='last_message',
            field=models.JSONField(null=True, verbose_name='Последнее сообщение в чате'),
        ),
    ]
