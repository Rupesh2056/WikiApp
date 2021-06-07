from django import forms

class add_form(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=2000,widget=forms.Textarea())

class edit_form(forms.Form):
    content = forms.CharField(max_length=2000,widget=forms.Textarea())