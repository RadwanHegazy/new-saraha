# Generated by Django 3.2.9 on 2022-02-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220203_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, default='static/website-images/profile.svg', upload_to='static/profile-images/'),
        ),
    ]
