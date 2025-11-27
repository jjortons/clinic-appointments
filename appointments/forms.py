from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "patient", "start_time", "status", "notes"]
        widgets = {
            "start_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
