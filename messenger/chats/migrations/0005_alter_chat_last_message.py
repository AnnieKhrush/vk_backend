# Generated by Django 4.1.2 on 2022-12-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_chat_last_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='last_message',
            field=models.CharField(max_length=256, null=True, verbose_name='Последнее сообщение в чате'),
        ),
    ]