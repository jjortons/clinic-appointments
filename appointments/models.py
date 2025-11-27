from django.db import models
from django.core.validators import RegexValidator


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.specialty})" if self.specialty else self.name


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patient_id = models.CharField(
        max_length=10,
        validators=[RegexValidator(
            regex=r'^\d{4}-\d{5}$',
            message='Patient ID must be in format 9999-99999'
        )],
        unique=True,
        blank=True,
        null=True
    )
    photo = models.ImageField(upload_to='patients/photos/', blank=True, null=True)
    voice_sample = models.FileField(upload_to='patients/voice_samples/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return f"{self.patient} with {self.doctor} at {self.start_time}"
