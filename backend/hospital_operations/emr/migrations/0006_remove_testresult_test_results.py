# Generated by Django 3.2.23 on 2024-03-07 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0005_rename_upload_results_testresult_test_results'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresult',
            name='test_results',
        ),
    ]
