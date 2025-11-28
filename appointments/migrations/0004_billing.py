from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_update_doctor_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('cancelled', 'Cancelled'), ('refunded', 'Refunded'), ('overdue', 'Overdue'), ('partially_paid', 'Partially Paid')], default='pending', max_length=20)),
                ('payment_method', models.CharField(blank=True, choices=[('cash', 'Cash'), ('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('insurance', 'Insurance'), ('other', 'Other')], max_length=20)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billings', to='appointments.appointment')),
            ],
            options={
                'verbose_name_plural': 'Billings',
                'ordering': ['-created_at'],
            },
        ),
    ]
