# Generated by Django 3.2.11 on 2022-02-07 23:59

# Standard Libraries
import json

# Django Imports
from django.db import migrations


def convert_to_jsonfield(apps, schema_editor):
    # Convert old string representations to JSON for the ``JSONfield``
    ReportTemplate = apps.get_model("reporting", "ReportTemplate")
    for entry in ReportTemplate.objects.all():
        try:
            entry.lint_result = json.loads(entry.lint_result)
            entry.save()
        except:
            entry.lint_result = {
                "result": "unknown",
                "warnings": [
                    "Need to re-run linting following your Ghostwriter upgrade",
                ],
                "errors": [],
            }
            entry.save()


class Migration(migrations.Migration):
    dependencies = [
        ("reporting", "0025_alter_reporttemplate_lint_result"),
    ]

    operations = [
        migrations.RunPython(convert_to_jsonfield),
    ]
