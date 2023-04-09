from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django.forms import ModelForm
from django import forms
from .models import Medicalstore
class MedicalstoreForm(ModelForm):
    class Meta:
        model=Medicalstore
        fields='__all__'

        widgets={
            'Medicine':forms.TextInput(attrs={'class':'form-control'}),
            'Brand':forms.TextInput(attrs={'class':'form-control'}),
            'Price':forms.TextInput(attrs={'class':'form-control'}),
        }