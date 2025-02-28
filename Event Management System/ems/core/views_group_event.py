from django.shortcuts import render, get_object_or_404, redirect
from .models import Group,Client,Event

TEMPLATE_PREFIX_EVENT = 'event/'
TEMPLATE_PREFIX_GROUP = 'groups/'

# Groups Dashboard
def groups_dashboard(request):
    groups = Group.objects.prefetch_related('events', 'client').all()
    return render(request, f'{TEMPLATE_PREFIX_GROUP}groups_dashboard.html', {'groups': groups})

def add_group(request):
    if request.method == 'POST':
        # Client Form Data
        client_name = request.POST.get('client_name')
        contact_info = request.POST.get('contact_info')

        # Group Form Data
        group_name = request.POST.get('group_name')
        date = request.POST.get('date')
        budget = request.POST.get('budget')
        status = request.POST.get('status')

        # If a new client is provided, create it
        if client_name and contact_info:
            client = Client.objects.create(
                client_name=client_name,
                contact_phone=contact_info
            )
        else:
            # Handle the case where no new client is added
            # Optional: Add a mechanism to select existing clients
            return render(request, f'{TEMPLATE_PREFIX_GROUP}add_group.html', {'error': 'Client information is required.'})

        # Create the group linked to the new client
        Group.objects.create(
            group_name=group_name,
            client=client,
            date=date,
            budget=budget,
            status=status
        )

        # Redirect to the Groups Dashboard
        return redirect('groups_dashboard')

    return render(request, f'{TEMPLATE_PREFIX_GROUP}add_group.html')

# Manage Group
def edit_group_details(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        group.group_name = request.POST.get('group_name')
        group.budget = request.POST.get('budget')
        group.status = request.POST.get('status')
        group.date = request.POST.get('date')
        group.save()
        return redirect('groups_dashboard')

    return render(request, f'{TEMPLATE_PREFIX_GROUP}edit_group_details.html', {'group': group})

# Manage Group Events
def manage_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    events = group.events.all()  # Fetch events associated with the group
    return render(request, f'{TEMPLATE_PREFIX_GROUP}manage_group.html', {'group': group, 'events': events})

# Add Event
def add_event(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_type = request.POST.get('event_type')
        date = request.POST.get('date')
        budget = request.POST.get('budget')
        description = request.POST.get('description')

        # Create the event linked to the group
        Event.objects.create(
            event_name=event_name,
            group=group,
            event_type=event_type,
            date=date,
            budget=budget,
            description=description
        )

        return redirect('manage_group', group_id=group_id)

    event_types = Event.EVENT_TYPES  # Pass event type choices to the template
    return render(request, f'{TEMPLATE_PREFIX_EVENT}add_event.html', {'group': group, 'event_types': event_types})

def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.event_name = request.POST.get('event_name')
        event.event_type = request.POST.get('event_type')
        event.date = request.POST.get('date')
        event.budget = request.POST.get('budget')
        event.description = request.POST.get('description')
        event.save()

        return redirect('manage_group', group_id=event.group.group_id)

    event_types = Event.EVENT_TYPES
    return render(request, f'{TEMPLATE_PREFIX_EVENT}edit_event.html', {'event': event, 'event_types': event_types})

# Manage Event (Basic Implementation)
def manage_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, f'{TEMPLATE_PREFIX_EVENT}manage_event.html', {'event': event})

