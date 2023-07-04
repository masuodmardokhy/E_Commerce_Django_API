from django import forms


class Sort_FilterForm(forms.Form):
    # filter = forms.CharField(max_length=30)
    sort_by = forms.CharField(max_length=30)
