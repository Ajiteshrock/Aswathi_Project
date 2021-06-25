# Generated by Django 3.0.7 on 2021-06-25 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myclass',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='material',
            name='file_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.MyClass'),
        ),
    ]