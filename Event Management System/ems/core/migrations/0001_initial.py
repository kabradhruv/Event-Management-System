# Generated by Django 5.1.4 on 2025-01-20 17:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=255)),
                ('contact_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ssp',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('rate_per_event', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('item_type', models.CharField(choices=[('Service', 'Service'), ('Setup', 'Setup'), ('Product', 'Product')], max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ssp_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=255)),
                ('service_type', models.CharField(max_length=255)),
                ('contact_info', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('rate_per_event', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='core.client')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255)),
                ('event_type', models.CharField(choices=[('Wedding', 'Wedding'), ('Corporate', 'Corporate'), ('Birthday', 'Birthday'), ('Others', 'Others')], max_length=50)),
                ('date', models.DateField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.group')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_type', models.CharField(choices=[('Quotation', 'Quotation'), ('Cost', 'Cost'), ('Task', 'Task'), ('Vendor Payment', 'Vendor Payment')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data', models.JSONField()),
                ('file_path', models.FileField(blank=True, null=True, upload_to='reports/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_reports', to='core.event')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='reports',
            field=models.ManyToManyField(blank=True, related_name='groups', to='core.report'),
        ),
        migrations.CreateModel(
            name='EventSsp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.event')),
                ('ssp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ssp')),
            ],
            options={
                'unique_together': {('event', 'ssp')},
            },
        ),
        migrations.AddField(
            model_name='event',
            name='ssps',
            field=models.ManyToManyField(related_name='events', through='core.EventSsp', to='core.ssp'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=50)),
                ('deadline', models.DateField()),
                ('is_reminder', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='core.event')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='core.vendor')),
            ],
        ),
    ]
