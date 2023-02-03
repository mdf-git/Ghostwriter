# Generated by Django 3.2.16 on 2022-12-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shepherd', '0043_staticserver_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='reset_dns',
            field=models.BooleanField(default=True, help_text='Reset DNS records (if possible) after this domain is used', verbose_name='Reset DNS'),
        ),
    ]
