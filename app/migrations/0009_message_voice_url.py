# Generated by Django 3.2.9 on 2022-02-06 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='voice_url',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]