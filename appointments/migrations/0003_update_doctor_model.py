from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_patient_fields'),
    ]

    operations = [
        # Remove the old name field
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        # Add first_name field
        migrations.AddField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        # Add last_name field
        migrations.AddField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        # Add registration_number field
        migrations.AddField(
            model_name='doctor',
            name='registration_number',
            field=models.CharField(blank=True, help_text='Medical license/registration number', max_length=50, null=True, unique=True),
        ),
        # Add clinic_address field
        migrations.AddField(
            model_name='doctor',
            name='clinic_address',
            field=models.TextField(blank=True),
        ),
        # Add clinic_hours field
        migrations.AddField(
            model_name='doctor',
            name='clinic_hours',
            field=models.CharField(blank=True, help_text='e.g., Mon-Fri 9AM-5PM', max_length=200),
        ),
        # Add clinic_phone field
        migrations.AddField(
            model_name='doctor',
            name='clinic_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        # Add photo field
        migrations.AddField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='doctors/photos/'),
        ),
        # Add comments field
        migrations.AddField(
            model_name='doctor',
            name='comments',
            field=models.TextField(blank=True, help_text='Additional notes about the doctor'),
        ),
    ]
