from django import forms

class AddressForm(forms.Form):
    source_address = forms.CharField(label='Source Address', max_length=255)
    destination_address = forms.CharField(label='Destination Address', max_length=255)
    