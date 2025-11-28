from django.db import models
from django.core.validators import RegexValidator


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100, blank=True)
    registration_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        help_text='Medical license/registration number'
    )
    clinic_address = models.TextField(blank=True)
    clinic_hours = models.CharField(
        max_length=200,
        blank=True,
        help_text='e.g., Mon-Fri 9AM-5PM'
    )
    clinic_phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='doctors/photos/', blank=True, null=True)
    comments = models.TextField(blank=True, help_text='Additional notes about the doctor')

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}" + (f" ({self.specialty})" if self.specialty else "")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


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
        ordering = ['-start_time']

    def __str__(self):
        return f"{self.patient} with Dr. {self.doctor.last_name} on {self.start_time.strftime('%Y-%m-%d %H:%M')}"


class Billing(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('partially_paid', 'Partially Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('insurance', 'Insurance'),
        ('other', 'Other'),
    ]
    
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='billings')
    invoice_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, blank=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, help_text='Service description or itemized list')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Billings'
    
    def save(self, *args, **kwargs):
        # Calculate total amount
        self.total_amount = self.amount + self.tax - self.discount
        # Generate invoice number if not provided
        if not self.invoice_number:
            import datetime
            self.invoice_number = f"INV-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)
    
    @property
    def balance_due(self):
        return (self.total_amount or 0) - self.amount_paid
    
    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.appointment.patient} - ${self.total_amount}"
