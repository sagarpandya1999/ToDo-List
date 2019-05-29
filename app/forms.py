from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=256,
                           widget=forms.TextInput(
                               attrs={
                                   #here you can mention styles and class and all th stuff you want to apply on input.

    }))