from django import forms
from .models import Appointment, Patient, Doctor, Billing


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'start_time', 'status', 'notes']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'patient_id', 'email', 'phone', 'photo', 'voice_sample']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'patient_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234-56789'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'voice_sample': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'patient_id': 'Patient ID (format: 0000-00000)',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'photo': 'Patient Photo',
            'voice_sample': 'Voice Sample',
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialty', 'registration_number', 
                  'clinic_address', 'clinic_hours', 'clinic_phone', 'photo', 'comments']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Cardiology'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medical License Number'}),
            'clinic_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Clinic Address'}),
            'clinic_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Mon-Fri 9AM-5PM'}),
            'clinic_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Clinic Phone Number'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional notes'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'specialty': 'Specialty',
            'registration_number': 'Registration Number',
            'clinic_address': 'Clinic Address',
            'clinic_hours': 'Clinic Hours',
            'clinic_phone': 'Clinic Phone',
            'photo': 'Doctor Photo',
            'comments': 'Comments',
        }


            

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['appointment', 'amount', 'tax', 'discount', 'payment_status', 
                  'payment_method', 'due_date', 'description', 'notes']
        widgets = {
            'appointment': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'tax': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'payment_status': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Service description'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Additional notes'}),
        }
        labels = {
            'amount': 'Service Amount ($)',
            'tax': 'Tax Amount ($)',
            'discount': 'Discount ($)',
            'payment_status': 'Payment Status',
            'payment_method': 'Payment Method',
            'due_date': 'Due Date',
            'description': 'Service Description',
            'notes': 'Notes',
        }
        }
