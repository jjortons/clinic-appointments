from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Appointment, Patient
from .forms import AppointmentForm, PatientForm


def appointment_list(request):
    appointments = Appointment.objects.select_related('doctor', 'patient').all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})


def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('appointment_list'))
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form})


def patient_list(request):
    patients = Patient.objects.all().order_by('last_name', 'first_name')
    return render(request, 'appointments/patient_list.html', {'patients': patients})


def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            patient = form.save()
            messages.success(request, f'Patient {patient.first_name} {patient.last_name} was added successfully!')
            return redirect(reverse('patient_list'))
    else:
        form = PatientForm()
    return render(request, 'appointments/patient_form.html', {'form': form, 'title': 'Add New Patient'})


def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    appointments = Appointment.objects.filter(patient=patient).order_by('-start_time')
    return render(request, 'appointments/patient_detail.html', {'patient': patient, 'appointments': appointments})


def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, f'Patient {patient.first_name} {patient.last_name} was updated successfully!')
            return redirect(reverse('patient_detail', args=[pk]))
    else:
        form = PatientForm(instance=patient)
    return render(request, 'appointments/patient_form.html', {'form': form, 'title': 'Edit Patient', 'patient': patient})
