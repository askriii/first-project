from django import forms
from .models import Bd

class BdForm(forms.ModelForm):
    class Meta:
        model = Bd
        fields = ('CIN','Nom', 'Prenom', 'Adresse', 'Email', 'Numerotelephone', 'Profession', 'Departement')

