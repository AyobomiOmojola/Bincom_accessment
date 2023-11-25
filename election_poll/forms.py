from django import forms
from .models import AnnouncedPuResults

class PartyPollingResultForm(forms.ModelForm):
    date_entered = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:

        model = AnnouncedPuResults
        fields = ['result_id','polling_unit_uniqueid','party_abbreviation','party_score','entered_by_user','date_entered']