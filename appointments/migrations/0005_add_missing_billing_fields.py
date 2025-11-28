from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_billing'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='billing',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='billing',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='billing',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
