from django import forms


class SearchForm(forms.Form):
    survelliance_key = forms.CharField(max_length=25)
