# Generated by Django 5.1.6 on 2025-07-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0004_alter_design_design_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
