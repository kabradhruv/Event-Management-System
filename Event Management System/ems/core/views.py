from django.db.models import Q  # For search and filter functionality
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Group,Client,Event,Vendor,VendorEventAssignment
from django.http import JsonResponse
from datetime import date







# Functions which are constant with different views

def get_events(request, group_id):
    events = Event.objects.filter(group_id=group_id)
    event_list = [{'event_id': event.event_id, 'event_name': event.event_name} for event in events]
    print("The event lsit are - ")
    print(event_list)
    return JsonResponse({'events': event_list})

def all_ssp(request):
    
    return 

@login_required
def home(request):
    return render(request, 'home.html')
