# Generated migration for Patient model changes

from django.core.validators import RegexValidator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
        migrations.AddField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                unique=True,
                validators=[RegexValidator(
                    regex=r'^\d{4}-\d{5}$',
                    message='Patient ID must be in format 9999-99999'
                )],
            ),
        ),
        migrations.AddField(
            model_name='patient',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='patients/photos/'),
        ),
        migrations.AddField(
            model_name='patient',
            name='voice_sample',
            field=models.FileField(blank=True, null=True, upload_to='patients/voice_samples/'),
        ),
    ]
