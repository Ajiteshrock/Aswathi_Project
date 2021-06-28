# Generated by Django 3.0.7 on 2021-06-27 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hod.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadOfDepartment',
            fields=[
                ('profile_pic', models.FileField(upload_to=hod.models.upload_profile)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
