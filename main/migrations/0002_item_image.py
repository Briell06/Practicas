# Generated by Django 5.2 on 2025-04-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
