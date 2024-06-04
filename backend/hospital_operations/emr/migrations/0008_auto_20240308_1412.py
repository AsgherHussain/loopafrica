# Generated by Django 3.2.23 on 2024-03-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0007_auto_20240307_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='date',
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='frmdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='todate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
