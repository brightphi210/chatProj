# Generated by Django 5.0.6 on 2024-07-03 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0004_remove_room_username_alter_message_room_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
