# Generated by Django 3.1.2 on 2021-08-03 21:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0010_auto_20210804_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='txn_id',
            field=models.CharField(blank=True, default=uuid.UUID('b5cc5a26-06a0-443e-81b5-c057f74f233a'), max_length=100),
        ),
    ]
