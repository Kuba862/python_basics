from django import forms
form .models import MyModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = [
            "title",
            "description",
        ]