# Generated by Django 5.0.7 on 2024-08-10 14:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_rename_area_useraddress_area"),
    ]

    operations = [
        migrations.RenameField(
            model_name="useraddress",
            old_name="area",
            new_name="Area",
        ),
    ]
