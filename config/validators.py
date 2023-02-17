
from django.core import validators
from django import forms

def min_length_3(value):
    if len(value)< 3:
        raise forms.ValidationError("Our Own Control Function At Least 3 Characters!")
