from django import forms
from .models import OrganisationEvent, Category

class OrganisationEventForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category")

    class Meta:
        model = OrganisationEvent
        fields = ['event_name', 'event_date', 'venue', 'description', 'category']
