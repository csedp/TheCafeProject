"""Generated by Django 4.1.3 on 2022-06-18 04:59"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """migration file for menu app"""

    dependencies = [
        ('menu', '0004_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dishName',
            field=models.CharField(max_length=35),
        ),
    ]
