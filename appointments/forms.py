from django import forms
from .models import Appointment, Patient


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'start_time', 'status', 'notes']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
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
            'patient_id': 'Patient ID (format: 9999-99999)',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'photo': 'Patient Photo',
            'voice_sample': 'Voice Sample',
        }
