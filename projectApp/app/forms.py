from django import forms

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    zip_code = forms.CharField(max_length=10, required=False)
    date = forms.DateField(widget = forms.SelectDateWidget, required=False)
    
