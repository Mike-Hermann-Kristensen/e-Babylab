# Generated by Django 3.1.14 on 2022-10-07 20:21

from django.db import migrations, models


def convert_datetime_to_float(apps, schema_editor):
    TrialResult = apps.get_model('experiments', 'TrialResult')
    for row in TrialResult.objects.all():
        row.start_time = row.start_time_old.timestamp()
        row.end_time = row.end_time_old.timestamp()
        row.save(update_fields=['start_time', 'end_time'])


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0059_auto_20221007_2221'),
    ]

    operations = [
        migrations.RunPython(convert_datetime_to_float, reverse_code=migrations.RunPython.noop),
    ]