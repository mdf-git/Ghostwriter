# Generated by Django 3.0.10 on 2021-03-18 21:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reporting", "0022_auto_20210211_2109"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="severity",
            options={
                "ordering": ["weight", "severity"],
                "verbose_name": "Severity rating",
                "verbose_name_plural": "Severity ratings",
            },
        ),
    ]
