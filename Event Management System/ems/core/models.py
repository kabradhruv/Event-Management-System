from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# SSP Table
class Ssp(models.Model):
    ITEM_TYPES = [
            ('Furniture', 'Furniture'),
            ('Decor', 'Decor'),
            ('Stage', 'Stage'),
            ('Setup', 'Setup'), # pre designed collections of different Item types
            ('Entrance', 'Entrance'),
            ('Services', 'Services'),
            ('Audio-Visual', 'Audio-Visual'),
            ('Stalls', 'Stalls'),
            ('Lighting', 'Lighting'),
            ('Miscellaneous', 'Miscellaneous'),
        ]
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    rate_per_event = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=255, blank=True, null=True)  # Comma-separated tags
    item_type = models.CharField(max_length=50, choices=ITEM_TYPES)
    image = models.ImageField(upload_to='ssp_images/', blank=True, null=True)  # Optional image field

    def __str__(self):
        return self.name

class Event(models.Model):
    EVENT_TYPES = [
        ('Wedding', 'Wedding'),
        ('Corporate', 'Corporate'),
        ('Birthday', 'Birthday'),
        ('Others', 'Others'),
    ]
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    date = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    ssps = models.ManyToManyField('Ssp', through='EventSsp', related_name='events')

    def __str__(self):
        return self.event_name

    def summary(self):
        return f"{self.event_name} ({self.event_type}) on {self.date}"
    
class EventSsp(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ssp = models.ForeignKey(Ssp, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        
        if self.quantity == 0:
            # If there's already an instance with this event and ssp, delete it
            existing_entry = EventSsp.objects.filter(event=self.event, ssp=self.ssp).first()
            if existing_entry:
                existing_entry.delete()
            return  # Skip saving the object

        # Check if an existing record with the same event and ssp exists
        existing_entry = EventSsp.objects.filter(event=self.event, ssp=self.ssp).first()

        if existing_entry:
            if self.pk == existing_entry.pk:
                # Updating the same entry, allow saving (e.g., updating quantity)
                super().save(*args, **kwargs)
            else:
                # Another entry with the same event and ssp exists, raise error
                raise ValidationError(f"The SSP '{self.ssp.name}' is already associated with the event '{self.event.event_name}'.")
        else:
            # No duplicate found, proceed with saving
            super().save(*args, **kwargs)

# Vendors Table
class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255)
    contact_info = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)  # Rating out of 5
    rate_per_event = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(null=True, blank=True)  # Optional field for additional details

    def __str__(self):
        return self.vendor_name


# Groups Table
class Group(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Upcoming', 'Upcoming'),
    ]
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='groups')
    date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    reports = models.ManyToManyField('Report', related_name='groups', blank=True)

    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ['-date']


# Clients Table
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.client_name

    class Meta:
        ordering = ['client_name']

# Tasks Table
class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    deadline = models.DateField()
    is_reminder = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name


class VendorEventAssignment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Partially Paid', 'Partially Paid'),
        ('Paid', 'Paid'),
    ]

    WORK_STATUS_CHOICE = [('In Progress', 'In Progress'), ('Completed', 'Completed')]
    
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="assignments")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="vendor_assignments")
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, related_name="vendor_assignments", blank=True, null=True)  # Optional
    role_description = models.TextField(blank=True, null=True)  # Optional text field describing the work
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Budget for this work
    date_assigned = models.DateField(auto_now_add=True)
    
    payment_status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending'
    )

    status = models.CharField(max_length=20, choices=WORK_STATUS_CHOICE, default='In Progress')
    
    payment_history = models.JSONField(default=list, blank=True)  # List of payments (date, amount)
    
    work_payment_mapping = models.JSONField(default=dict, blank=True)  # Store work: payment mapping
    
    def __str__(self):
        return f"{self.vendor.vendor_name} assigned to {self.event.event_name}"


    
# Reports Table
class Report(models.Model):
    REPORT_TYPES = [
        ('Quotation', 'Quotation'),
        ('Cost', 'Cost'),
        ('Task', 'Task'),
        ('Vendor Payment', 'Vendor Payment'),
    ]

    report_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_reports', blank=True, null=True)  # Changed related_name here
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()  # Stores detailed report data
    file_path = models.FileField(upload_to='reports/', blank=True, null=True)

    def __str__(self):
        return f"{self.report_type} - {self.report_id}"
