from django import forms

class SearchForm(forms.Form):
    entry = forms.CharField(label="Search Encyclopedia", min_length=1)
