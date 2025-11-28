from django.contrib import admin
from .models import Doctor, Patient, Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'specialty', 'registration_number', 'clinic_phone')
    search_fields = ('first_name', 'last_name', 'specialty', 'registration_number')
    list_filter = ('specialty',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'specialty', 'registration_number', 'photo')
        }),
        ('Clinic Information', {
            'fields': ('clinic_address', 'clinic_hours', 'clinic_phone')
        }),
        ('Additional Information', {
            'fields': ('comments',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patient_id', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'patient_id', 'email', 'phone')
    list_filter = ('last_name',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'patient_id')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone')
        }),
        ('Media Files', {
            'fields': ('photo', 'voice_sample'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'start_time', 'status')
    list_filter = ('status', 'doctor')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name')
    ordering = ('start_time',)
