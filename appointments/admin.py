from django.contrib import admin
from .models import Doctor, Patient, Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')
    search_fields = ('name', 'specialty')


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
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__name')
    ordering = ('start_time',)
