# Generated by Django 3.0.10 on 2021-06-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shepherd", "0017_domain_reset_dns"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transientserver",
            name="note",
            field=models.TextField(
                blank=True,
                help_text="Use this area to provide project-related notes, such as how the server will be used",
                null=True,
                verbose_name="Notes",
            ),
        ),
    ]
