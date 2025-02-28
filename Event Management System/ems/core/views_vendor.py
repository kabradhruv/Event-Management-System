from django.db.models import Q  # For search and filter functionality
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Group,Client,Event,Vendor,VendorEventAssignment
from django.http import JsonResponse
from datetime import date

TEMPLATE_PREFIX = 'vendor/'

def add_vendor(request):
    if request.method == 'POST':
        vendor_name = request.POST.get('vendor_name')
        service_type = request.POST.get('service_type')
        contact_info = request.POST.get('contact_info')
        rating = request.POST.get('rating')
        rate_per_event = request.POST.get('rate_per_event')
        details = request.POST.get('details')  # New field

        # Input Validation (optional)
        if not vendor_name or not service_type or not contact_info or not rate_per_event:
            messages.error(request, "All fields except 'Rating' and 'Details' are required.")
            return render(request, f'{TEMPLATE_PREFIX}add_vendor.html')

        try:
            # Create the vendor record
            Vendor.objects.create(
                vendor_name=vendor_name,
                service_type=service_type,
                contact_info=contact_info,
                rating=rating if rating else None,
                rate_per_event=rate_per_event,
                details=details  # Save details
            )
            messages.success(request, "Vendor added successfully!")
            return redirect('vendor_dashboard')  # Redirect to the Vendor Dashboard
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

    return render(request, f'{TEMPLATE_PREFIX}add_vendor.html')


def vendor_dashboard(request):
    query = request.GET.get('query', '')  # Get search query
    service_type = request.GET.get('service_type', '')  # Get filter for service type
    min_rating = request.GET.get('min_rating', '')  # Get filter for minimum rating

    # Filter vendors based on search and filters
    vendors = Vendor.objects.all()
    if query:
        vendors = vendors.filter(
            Q(vendor_name__icontains=query) |
            Q(contact_info__icontains=query)
        )
    if service_type:
        vendors = vendors.filter(service_type__icontains=service_type)
    if min_rating:
        try:
            vendors = vendors.filter(rating__gte=float(min_rating))
        except ValueError:
            pass

    return render(request, f'{TEMPLATE_PREFIX}vendor_dashboard.html', {
        'vendors': vendors,
        'query': query,
        'service_type': service_type,
        'min_rating': min_rating,
    })


def edit_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, vendor_id=vendor_id)
    
    if request.method == 'POST':
        # Update vendor fields based on the form data
        vendor.vendor_name = request.POST.get('vendor_name')
        vendor.service_type = request.POST.get('service_type')
        vendor.contact_info = request.POST.get('contact_info')
        vendor.rating = request.POST.get('rating')
        vendor.rate_per_event = request.POST.get('rate_per_event')
        vendor.details = request.POST.get('details', '')
        
        vendor.save()
        return redirect('vendor_dashboard')  # Redirect to vendor dashboard after save

    return render(request, f'{TEMPLATE_PREFIX}edit_vendor.html', {'vendor': vendor})


def sge_vendor(request):
    if request.method == 'POST':
        group_id = request.POST.get('group')
        event_id = request.POST.get('event')
        if group_id and event_id:
            # Process the selected group and event
            return redirect(f'assign_vendor/?event_id={event_id}')
        else:
            # Handle the case where group or event is not selected
            return render(request, 'select_group_event.html', {'groups': Group.objects.all(), 'error': 'Please select both a group and an event.'})
    else:
        return render(request, 'select_group_event.html', {'groups': Group.objects.all()})


def assign_vendor(request):
    print("IN assign vendor")
    if request.method == "POST":
        vendor_id = request.POST.get('vendor')
        event_id = request.POST.get('event')
        role_description = request.POST.get('role_description', '').strip()
        budget = request.POST.get('budget', None)
        action = request.POST.get('action')

        # Validation
        if not vendor_id or not event_id:
            messages.error(request, "Vendor and Event fields are required.")
            return render(request, f'{TEMPLATE_PREFIX}assign_vendor.html', {
                'groups': Group.objects.all(),
                'vendors': Vendor.objects.all(),
                'events': Event.objects.all(),
            })

        # Fetch Vendor and Event
        try:
            vendor = Vendor.objects.get(vendor_id=vendor_id)
        except Vendor.DoesNotExist:
            messages.error(request, "Selected vendor does not exist.")
            return redirect('assign_vendor')

        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            messages.error(request, "Selected event does not exist.")
            return redirect('assign_vendor')

        # Check if an assignment already exists
        existing_assignment = VendorEventAssignment.objects.filter(vendor=vendor, event=event).first()
        if existing_assignment:
            # Redirect to manage_assignment if assignment exists
            messages.info(request, f"An assignment for {vendor.vendor_name} and {event.event_name} already exists.")
            return redirect('manage_assignment', assignment_id=existing_assignment.id)

        # Handle optional fields
        budget = float(budget) if budget else None

        # Create a new Vendor Event Assignment
        new_assignment = VendorEventAssignment.objects.create(
            vendor=vendor,
            event=event,
            role_description=role_description,
            budget=budget,
        )

        # Action Handling
        if action == "save":
            messages.success(request, f"Assignment for {vendor.vendor_name} saved successfully.")
            return redirect('vendor_dashboard')

        elif action == "save_and_manage":
            messages.success(request, f"Assignment for {vendor.vendor_name} saved. Redirecting to manage.")
            # return redirect('manage_assignment', assignment_id=new_assignment.id)
            return redirect('manage_assignment', assignment_id=new_assignment.id)

    # GET request handling
    vendor_id = request.GET.get('vendor_id')
    event_id = request.GET.get('event_id')
    print("Event ID - " , event_id)
    vendor = None
    group = None
    event = None

    if vendor_id:
        try:
            vendor = Vendor.objects.get(vendor_id=vendor_id)
        except Vendor.DoesNotExist:
            pass

    if event_id:
        try:
            event = Event.objects.get(event_id=event_id)
            group = event.group
        except Event.DoesNotExist:
            pass

    return render(request, f'{TEMPLATE_PREFIX}assign_vendor.html', {
        'vendor': vendor,
        'group': group,
        'event': event,
        'groups': Group.objects.all(),
        'vendors': Vendor.objects.all(),
        'events': Event.objects.all(),
    })


def manage_assignment(request, assignment_id):
    # Fetch the assignment details
    assignment = get_object_or_404(VendorEventAssignment, id=assignment_id)

    if request.method == "POST":
        # Handle status update (Mark assignment as completed)
        if "mark_completed" in request.POST:
            assignment.status = "Completed"
            assignment.save()
            messages.success(request, f"Assignment marked as completed.")
            return redirect("manage_assignment", assignment_id=assignment.id)

    # Render the manage assignment page
    return render(request, f"{TEMPLATE_PREFIX}manage_assignment.html", {
        "assignment": assignment,
    })


def assignment_detail(request, vendor_id):
    # Fetch the vendor
    vendor = get_object_or_404(Vendor, vendor_id=vendor_id)

    # Fetch all assignments for the vendor
    assignments = VendorEventAssignment.objects.filter(vendor=vendor)

    return render(request, f'{TEMPLATE_PREFIX}assignment_detail.html', {
        'vendor': vendor,
        'assignments': assignments,
    })


def record_payment(request, assignment_id):
    # Fetch the assignment from the database
    assignment = get_object_or_404(VendorEventAssignment, id=assignment_id)

    if request.method == "POST":
        # Retrieve form data from the POST request
        payment_amount = request.POST.get("payment_amount")  # Required field
        payment_date = request.POST.get("payment_date")  # Optional, defaults to today
        payment_method = request.POST.get("payment_method", "")  # Optional
        notes = request.POST.get("notes", "")  # Optional
        payment_status = request.POST.get("payment_status", "Partial")  # Default to Partial
        work_payment_mapping = request.POST.get("work_payment_mapping", "")  # Work details

        # Validate payment amount
        if not payment_amount or float(payment_amount) <= 0:
            messages.error(request, "Payment amount must be greater than zero.")
            return redirect("record_payment", assignment_id=assignment.id)

        try:
            # Convert payment amount to float
            payment_amount = float(payment_amount)
        except ValueError:
            messages.error(request, "Invalid payment amount format.")
            return redirect("record_payment", assignment_id=assignment.id)

        # Process "work_payment_mapping" input
        work_payment_mapping_list = [work.strip() for work in work_payment_mapping.split(",") if work.strip()]
        if not work_payment_mapping_list:
            messages.error(request, "Please specify at least one work entry.")
            return redirect("record_payment", assignment_id=assignment.id)

        # Distribute the payment equally or add all under the specified works
        work_payment_data = {}
        payment_per_work = payment_amount / len(work_payment_mapping_list)  # Divide payment equally
        for work in work_payment_mapping_list:
            work_payment_data[work] = payment_per_work

        # Update the work_payment_mapping field in the assignment
        assignment.work_payment_mapping.update(work_payment_data)

        # Update the payment history in the assignment
        payment_entry = {
            "date": payment_date or str(date.today()),  # Default to today's date if not provided
            "amount": payment_amount,
            "method": payment_method,
            "notes": notes,
        }
        assignment.payment_history.append(payment_entry)

        # Update the assignment status
        assignment.status = "Completed" if payment_status == "Full" else "In Progress"

        # Save the updated assignment
        assignment.save()

        # Provide feedback and redirect to manage assignment
        messages.success(request, "Payment recorded successfully!")
        return redirect("manage_assignment", assignment_id=assignment.id)

    return render(request, f"{TEMPLATE_PREFIX}record_payment.html", {"assignment": assignment})


