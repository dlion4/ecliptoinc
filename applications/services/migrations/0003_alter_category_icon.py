# Generated by Django 4.2.11 on 2024-04-05 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.TextField(blank=True, null=True),
        ),
    ]
