from django import forms

class FindLocationForm(forms.Form):
	latitude=forms.FloatField()
	longitude=forms.FloatField()