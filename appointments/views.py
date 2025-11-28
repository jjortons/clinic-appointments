from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Appointment, Patient, Doctor, Billing
from .forms import AppointmentForm, PatientForm, DoctorForm, BillingForm


# Dashboard view
def dashboard(request):
    doctors_count = Doctor.objects.count()
    patients_count = Patient.objects.count()
    appointments_count = Appointment.objects.count()
    recent_appointments = Appointment.objects.select_related('doctor', 'patient').order_by('-start_time')[:5]
    return render(request, 'appointments/dashboard.html', {
        'doctors_count': doctors_count,
        'patients_count': patients_count,
        'appointments_count': appointments_count,
        'recent_appointments': recent_appointments,
    })


# ==================== DOCTOR VIEWS ====================
def doctor_list(request):
    doctors = Doctor.objects.all().order_by('last_name', 'first_name')
    return render(request, 'appointments/doctor_list.html', {'doctors': doctors})


def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('-start_time')
    return render(request, 'appointments/doctor_detail.html', {'doctor': doctor, 'appointments': appointments})


def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save()
            messages.success(request, f'Dr. {doctor.first_name} {doctor.last_name} was added successfully!')
            return redirect(reverse('doctor_list'))
    else:
        form = DoctorForm()
    return render(request, 'appointments/doctor_form.html', {'form': form, 'title': 'Add New Doctor'})


def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dr. {doctor.first_name} {doctor.last_name} was updated successfully!')
            return redirect(reverse('doctor_detail', args=[pk]))
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'appointments/doctor_form.html', {'form': form, 'title': 'Edit Doctor', 'doctor': doctor})


def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        name = f'Dr. {doctor.first_name} {doctor.last_name}'
        doctor.delete()
        messages.success(request, f'{name} was deleted successfully!')
        return redirect(reverse('doctor_list'))
    return render(request, 'appointments/doctor_confirm_delete.html', {'doctor': doctor})


# ==================== PATIENT VIEWS ====================
def patient_list(request):
    patients = Patient.objects.all().order_by('last_name', 'first_name')
    return render(request, 'appointments/patient_list.html', {'patients': patients})


def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    appointments = Appointment.objects.filter(patient=patient).order_by('-start_time')
    return render(request, 'appointments/patient_detail.html', {'patient': patient, 'appointments': appointments})


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


def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        name = f'{patient.first_name} {patient.last_name}'
        patient.delete()
        messages.success(request, f'Patient {name} was deleted successfully!')
        return redirect(reverse('patient_list'))
    return render(request, 'appointments/patient_confirm_delete.html', {'patient': patient})


# ==================== APPOINTMENT VIEWS ====================
def appointment_list(request):
    appointments = Appointment.objects.select_related('doctor', 'patient').all().order_by('-start_time')
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})


def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment.objects.select_related('doctor', 'patient'), pk=pk)
    return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})


def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(request, 'Appointment was created successfully!')
            return redirect(reverse('appointment_list'))
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form, 'title': 'Create New Appointment'})


def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment was updated successfully!')
            return redirect(reverse('appointment_detail', args=[pk]))
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/appointment_form.html', {'form': form, 'title': 'Edit Appointment', 'appointment': appointment})


def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment was deleted successfully!')
        return redirect(reverse('appointment_list'))
    return render(request, 'appointments/appointment_confirm_delete.html', {'appointment': appointment})


# ==================== BILLING VIEWS ====================

def billing_list(request):
    billings = Billing.objects.select_related('appointment__doctor', 'appointment__patient').all()
    return render(request, 'appointments/billing_list.html', {'billings': billings})

def billing_detail(request, pk):
    billing = get_object_or_404(Billing.objects.select_related('appointment__doctor', 'appointment__patient'), pk=pk)
    return render(request, 'appointments/billing_detail.html', {'billing': billing})

def billing_create(request, appointment_pk=None):
    appointment = None
    if appointment_pk:
        appointment = get_object_or_404(Appointment, pk=appointment_pk)
    
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            billing = form.save()
            messages.success(request, f'Invoice {billing.invoice_number} was created successfully!')
            return redirect(reverse('appointments:billing_detail', args=[billing.pk]))
    else:
        initial = {}
        if appointment:
            initial['appointment'] = appointment
        form = BillingForm(initial=initial)
    
    return render(request, 'appointments/billing_form.html', {
        'form': form,
        'title': 'Create Invoice',
        'appointment': appointment
    })

def billing_edit(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=billing)
        if form.is_valid():
            form.save()
            messages.success(request, f'Invoice {billing.invoice_number} was updated successfully!')
            return redirect(reverse('appointments:billing_detail', args=[pk]))
    else:
        form = BillingForm(instance=billing)
    return render(request, 'appointments/billing_form.html', {'form': form, 'title': 'Edit Invoice', 'billing': billing})

def billing_delete(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    if request.method == 'POST':
        invoice_number = billing.invoice_number
        billing.delete()
        messages.success(request, f'Invoice {invoice_number} was deleted successfully!')
        return redirect(reverse('appointments:billing_list'))
    return render(request, 'appointments/billing_confirm_delete.html', {'billing': billing})

def billing_mark_paid(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    if request.method == 'POST':
        billing.payment_status = 'paid'
        billing.amount_paid = billing.total_amount
        from django.utils import timezone
        billing.payment_date = timezone.now()
        billing.save()
        messages.success(request, f'Invoice {billing.invoice_number} marked as paid!')
    return redirect(reverse('appointments:billing_detail', args=[pk]))
