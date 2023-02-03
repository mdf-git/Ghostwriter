# Generated by Django 3.2.11 on 2022-02-09 18:24

# Standard Libraries
import json

# Django Imports
from django.db import migrations


def convert_to_jsonfield(apps, schema_editor):
    # Convert old string representations to JSON for the ``JSONfield``
    Domain = apps.get_model("shepherd", "Domain")
    for entry in Domain.objects.all():
        # Run ``Domain`` model's old ``get_list()`` method to convert ``str`` to JSON
        try:
            record = {}
            json_acceptable_string = entry.dns_record.replace('"', "").replace("'", '"')
            if json_acceptable_string:
                record = json.loads(json_acceptable_string)
            entry.dns = record
            entry.save()
        except:
            entry.dns = {}
            entry.save()


class Migration(migrations.Migration):
    dependencies = [
        ("shepherd", "0036_auto_20220209_1815"),
    ]

    operations = [
        migrations.RunPython(convert_to_jsonfield),
    ]
