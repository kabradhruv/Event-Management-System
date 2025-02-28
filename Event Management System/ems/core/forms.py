# forms.py
from django import forms
from .models import Event, Ssp, EventSsp,Group


from django import forms
from .models import Ssp

class SspForm(forms.ModelForm):
    class Meta:
        model = Ssp
        fields = ['name', 'rate_per_event', 'tags', 'item_type', 'image']