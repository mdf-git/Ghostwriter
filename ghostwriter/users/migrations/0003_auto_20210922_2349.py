# Generated by Django 3.1.13 on 2021-09-22 23:49

import timezone_field.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_auto_20190729_1749"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="Enter a phone number for this user",
                max_length=50,
                null=True,
                verbose_name="Phone",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="timezone",
            field=timezone_field.fields.TimeZoneField(
                default="America/Los_Angeles",
                help_text="Primary timezone of the client",
                verbose_name="User's Timezone",
            ),
        ),
    ]
