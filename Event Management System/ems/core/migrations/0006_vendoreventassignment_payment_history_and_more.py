# Generated by Django 5.1.4 on 2025-01-22 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_vendor_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendoreventassignment',
            name='payment_history',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name='vendoreventassignment',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Partially Paid', 'Partially Paid'), ('Paid', 'Paid')], default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='vendoreventassignment',
            name='work_payment_mapping',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
