# Generated by Django 2.2.3 on 2019-11-22 23:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shepherd", "0007_auto_20191029_1636"),
    ]

    operations = [
        migrations.AlterField(
            model_name="domain",
            name="auto_renew",
            field=models.BooleanField(
                default=True,
                help_text="Whether or not the domain is set to renew automatically with the registrar",
                verbose_name="Auto Renew",
            ),
        ),
    ]
