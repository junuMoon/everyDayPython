# Generated by Django 3.2 on 2021-04-22 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_alter_report_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('created',)},
        ),
    ]