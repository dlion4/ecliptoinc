# Generated by Django 4.2.11 on 2024-04-12 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_position_salary_position_max_salary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='expiry',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2024, 4, 12, 14, 15, 12, 278306, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]