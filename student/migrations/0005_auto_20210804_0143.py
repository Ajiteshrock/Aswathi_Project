# Generated by Django 3.1.2 on 2021-08-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210729_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='academic_season',
            field=models.CharField(choices=[('fall', 'Fall'), ('spring', 'Spring'), ('summer_i', 'Summer I'), ('summer_ii', 'Summer II')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='application_fee',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('missing', 'Missing'), ('not_applicable', 'Not Applicable')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='application_form_completed',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('missing', 'Missing'), ('not_applicable', 'Not Applicable')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='apply_as',
            field=models.CharField(choices=[('freshman', 'Fresh man'), ('transfer', 'Transfer'), ('foundation', 'Foundation'), ('returning', 'Returning'), ('visiting', 'Visiting')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='birth_place',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name of the city where you were born'),
        ),
        migrations.AddField(
            model_name='student',
            name='emergency_contact_city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='emergency_contact_country',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='emergency_contact_email',
            field=models.EmailField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='emergency_contact_first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='emergency_contact_last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='emergency_contact_mobile',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='emergency_contact_relationship',
            field=models.CharField(choices=[('father', 'Father'), ('mother', 'Mother'), ('son', 'Son'), ('daughter', 'Daugther'), ('brother', 'Brother'), ('sister', 'Sister'), ('husband', 'Husband'), ('wife', 'Wife'), ('uncle', 'Uncle'), ('aunt', 'Aunt')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='emergency_contact_telephone_number',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='emirates_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='emirates_id_expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='english_language_test_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='english_language_test_name',
            field=models.CharField(choices=[('tofel', 'TOFEL'), ('ielts', 'IELTS')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='english_language_test_score',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='english_language_test_score_card',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('missing', 'Missing'), ('not_applicable', 'Not Applicable')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='high_school_academic_year',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='high_school_certificate',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('missing', 'Missing'), ('not_applicable', 'Not Applicable')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='high_school_certificate_type',
            field=models.CharField(choices=[('general_secondary', 'General Secondary Certificate'), ('high_school_diploma', 'High School Diploma'), ('british_certificate', 'British Certificate'), ('ib', 'IB')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='high_school_city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='high_school_country',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='high_school_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='high_school_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='medical_insurance',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('missing', 'Missing'), ('not_applicable', 'Not Applicable')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='national_card',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('missing', 'Missing'), ('not_applicable', 'Not Applicable')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='passport_expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='passport_issue_place',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='passport_number',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='passport_size_photos',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('missing', 'Missing'), ('not_applicable', 'Not Applicable')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='post_box_city',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='study_mode',
            field=models.CharField(choices=[('day', 'Day'), ('evening', 'Evening'), ('weekend', 'Weekend')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='transfer_college_academic_year',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='transfer_college_certificate',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('missing', 'Missing'), ('not_applicable', 'Not Applicable')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='transfer_college_city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='transfer_college_country',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='transfer_college_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='transfer_college_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='uae_residency_visa',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('missing', 'Missing'), ('not_applicable', 'Not Applicable')], default='', max_length=100),
        ),
    ]