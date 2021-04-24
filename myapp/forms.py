from django import forms

class GroupForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)


class StudenFrom(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, label="Nombre",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Nombre",
                'class': 'form-control',
            }
        ))

    last_name = forms.CharField(max_length=30, required=True, label="Apellido",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Apellido",
                'class': 'form-control',
            }
        ))