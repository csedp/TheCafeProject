"""Generated by Django 5.1.7 on 2022-06-15 11:12"""

from django.db import migrations


class Migration(migrations.Migration):
    """migration file for menu app"""

    dependencies = [
        ("menu", "0002_category"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Menu",
        ),
    ]
