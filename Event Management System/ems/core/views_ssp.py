from django.shortcuts import render, get_object_or_404, redirect
from .models import Group, Event, EventSsp ,Ssp
from .forms import SspForm
from django.contrib import messages

TEMPLATE_PREFIX = "ssp/"

def add_ssp(request):
    if request.method == 'POST':
        form = SspForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = SspForm()
    return render(request, f'{TEMPLATE_PREFIX}add_ssp.html', {'form': form})

def sge_ssp(request):
    if request.method == 'POST':
        group_id = request.POST.get('group')
        event_id = request.POST.get('event')
        if group_id and event_id:
            # Process the selected group and event
            return redirect('event_ssp_list', event_id=event_id)
        else:
            # Handle the case where group or event is not selected
            return render(request, 'select_group_event.html', {'groups': Group.objects.all(), 'error': 'Please select both a group and an event.'})
    else:
        return render(request, 'select_group_event.html', {'groups': Group.objects.all()})


def link_ssp_to_event(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)

    # Retrieve SSPs not currently associated with the event
    associated_ssps = EventSsp.objects.filter(event=event).values_list('ssp_id', flat=True)
    available_ssps = Ssp.objects.exclude(item_id__in=associated_ssps)  # Use 'item_id' instead of 'id'
    
    if request.method == 'POST':
        selected_ssps = request.POST.getlist('ssps')  # List of selected SSP IDs
        quantities = request.POST.getlist('quantities')  # Corresponding quantities

        # Process only the selected SSPs
        for ssp_id, quantity in zip(selected_ssps, quantities):
            if int(quantity) > 0:  # Ensure quantity is provided
                ssp = get_object_or_404(Ssp, item_id=ssp_id)
                EventSsp.objects.create(event=event, ssp=ssp, quantity=int(quantity))

        return redirect('event_ssp_list', event_id=event.event_id)

    context = {
        'event': event,
        'ssps': available_ssps,
    }
    return render(request, f'{TEMPLATE_PREFIX}link_ssp_to_event.html', context)

def event_ssp_list(request, event_id):
    event = Event.objects.get(event_id=event_id)
    ssps = EventSsp.objects.filter(event=event)
    print("The associated ssp of event " + event.event_name + " are - ")
    return render(request, f'{TEMPLATE_PREFIX}event_ssp_list.html', {'event': event, 'ssps': ssps})

def update_ssp_quantity(request, event_id, item_id):
    event = Event.objects.get(event_id=event_id)
    ssp = Ssp.objects.get(item_id=item_id)
    event_ssp = EventSsp.objects.get(event=event, ssp=ssp)

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        event_ssp.quantity = quantity
        event_ssp.save()
        return redirect('event_ssp_list', event_id=event.event_id)

    return redirect('event_ssp_list', event_id=event.event_id)

def remove_ssp_from_event(request, event_id, item_id):
    event = Event.objects.get(event_id=event_id)
    ssp = Ssp.objects.get(item_id=item_id)
    event_ssp = EventSsp.objects.get(event=event, ssp=ssp)
    event_ssp.delete()
    return redirect('event_ssp_list', event_id=event.event_id)


# Code for listing SSP , updating and removing from the database
def all_ssps(request):
    """View to display all SSPs."""
    ssps = Ssp.objects.all()
    return render(request, f'{TEMPLATE_PREFIX}all_ssp.html', {'ssps': ssps})


def update_all_ssps(request):
    """Handle bulk updates for SSPs."""
    if request.method == 'POST':
        # Loop through all SSPs
        for ssp in Ssp.objects.all():
            # Fetch updated values from POST data
            ssp.name = request.POST.get(f'name_{ssp.item_id}')
            ssp.rate_per_event = request.POST.get(f'rate_{ssp.item_id}')
            ssp.tags = request.POST.get(f'tags_{ssp.item_id}')
            ssp.item_type = request.POST.get(f'type_{ssp.item_id}')
            ssp.save()

        messages.success(request, 'All SSPs updated successfully!')
        return redirect('all_ssps')



def remove_ssp(request, ssp_id):
    """View to handle removing an SSP."""
    ssp = get_object_or_404(Ssp, pk=ssp_id)

    if request.method == 'POST':
        ssp_name = ssp.name
        ssp.delete()
        messages.success(request, f'SSP "{ssp_name}" removed successfully!')
        return redirect('all_ssps')

    return render(request, f'{TEMPLATE_PREFIX}all_ssp.html')