# Generated by Django 4.1.5 on 2023-02-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MeHealth", "0002_doctors_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctors",
            name="profile_image",
            field=models.ImageField(null=True, upload_to="media/doctor_profile/"),
        ),
    ]