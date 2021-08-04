# Generated by Django 3.1.2 on 2021-08-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('superadmin', 'Super Admin'), ('student', 'Student'), ('teacher', 'Teacher'), ('hod', 'Head of Department'), ('hr', 'HR'), ('accountant', 'Accountant'), ('registrar', 'Registrar')], default='', max_length=50),
        ),
    ]
