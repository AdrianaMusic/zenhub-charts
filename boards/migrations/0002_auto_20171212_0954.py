# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 09:54
from __future__ import unicode_literals

from django.db import migrations, models
from boards.models import Issue, Transfer

def update_latest_transfer_date(pp, schema_editor):
    for issue in Issue.objects.filter(latest_transfer_date__isnull=True):
        matching_transfer = Transfer.objects.filter(issue_id=issue.id).first()
        issue.latest_transfer_date = matching_transfer.transfered_at
        issue.save()


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        # First set the `latest_transfer_date` of the issue to the `Boards.Transfer.transfered_at` date.
        migrations.RunPython(code=update_latest_transfer_date),
        migrations.AlterField(
            model_name='issue',
            name='latest_transfer_date',
            field=models.DateTimeField(),
        ),
    ]