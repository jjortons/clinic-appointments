from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Doctor URLs
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/create/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/<int:pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),
    
    # Patient URLs
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    
    # Appointment URLs
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/<int:pk>/edit/', views.appointment_edit, name='appointment_edit'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),

        # Billing URLs
    path('billing/', views.billing_list, name='billing_list'),
    path('billing/create/', views.billing_create, name='billing_create'),
    path('billing/create/<int:appointment_pk>/', views.billing_create, name='billing_create_for_appointment'),
    path('billing/<int:pk>/', views.billing_detail, name='billing_detail'),
    path('billing/<int:pk>/edit/', views.billing_edit, name='billing_edit'),
    path('billing/<int:pk>/delete/', views.billing_delete, name='billing_delete'),
    path('billing/<int:pk>/mark-paid/', views.billing_mark_paid, name='billing_mark_paid'),
]
