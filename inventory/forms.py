from django import forms
from .models import *

class BonecasForm(forms.ModelForm):
    class Meta:
        model = Bonecas
        fields = ('nome', 'price', 'amount', 'status', 'issues')

class BonecosForm(forms.ModelForm):
    class Meta:
        model = Bonecos
        fields = ('nome', 'price', 'amount', 'status', 'issues')

class CarrosForm(forms.ModelForm):
    class Meta:
        model = Carros
        fields = ('nome', 'price', 'amount', 'status', 'issues')

class JogosForm(forms.ModelForm):
    class Meta:
        model = Jogos
        fields = ('nome', 'price', 'amount', 'status', 'issues')

class BrindesForm(forms.ModelForm):
    class Meta:
        model = Brindes
        fields = ('nome', 'price', 'amount', 'status', 'issues')

class OutrosForm(forms.ModelForm):
    class Meta:
        model = Outros
        fields = ('nome', 'price', 'amount', 'status', 'issues')


        #to do rest