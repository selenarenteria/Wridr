# Generated by Django 4.0.3 on 2022-03-11 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
    ]
