# Generated by Django 4.2.4 on 2023-08-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_remove_skill_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
