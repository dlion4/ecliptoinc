# Generated by Django 4.2.11 on 2024-04-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_position_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='salary',
        ),
        migrations.AddField(
            model_name='position',
            name='max_salary',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='position',
            name='min_salary',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]