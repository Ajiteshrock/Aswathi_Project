# Generated by Django 3.0.7 on 2021-07-08 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountant', '0001_initial'),
        ('course', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Degree'),
        ),
        migrations.AddField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]