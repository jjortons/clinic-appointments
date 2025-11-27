from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Appointment
from .forms import AppointmentForm

def appointment_list(request):
    appointments = Appointment.objects.select_related("doctor", "patient").all()
    return render(request, "appointments/appointment_list.html", {"appointments": appointments})


def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("appointment_list"))
    else:
        form = AppointmentForm()
    return render(request, "appointments/appointment_form.html", {"form": form})
