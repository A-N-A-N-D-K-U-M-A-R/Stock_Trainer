# Generated by Django 4.1.2 on 2022-10-06 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0003_alter_profile_image_field_alter_profile_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="email_id",
        ),
    ]
