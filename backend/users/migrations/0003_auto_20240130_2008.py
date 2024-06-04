# Generated by Django 3.2.23 on 2024-01-30 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_patientinfo_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('patient', 'Patient'), ('healthcare_provider', 'Healthcare Provider'), ('doctor', 'doctor'), ('instructor', 'instructor'), ('admin', 'Admin'), ('accountant', 'Accountant'), ('sales', 'Sales'), ('others', 'Others')], default='patient', max_length=20),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('about_instructor', models.TextField(blank=True, null=True)),
                ('specialized', models.TextField(blank=True, null=True)),
                ('qualification', models.CharField(blank=True, max_length=255, null=True, verbose_name='qualification')),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('last_updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instructor_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('about_doctor', models.TextField(blank=True, null=True)),
                ('specialized', models.TextField(blank=True, null=True)),
                ('qualification', models.CharField(blank=True, max_length=255, null=True, verbose_name='qualification')),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('last_updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]