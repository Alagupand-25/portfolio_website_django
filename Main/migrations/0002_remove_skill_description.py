# Generated by Django 4.2.4 on 2023-08-18 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='description',
        ),
    ]
