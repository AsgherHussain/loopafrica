# Generated by Django 3.2.23 on 2024-03-07 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0004_auto_20240307_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testresult',
            old_name='upload_results',
            new_name='test_results',
        ),
    ]
