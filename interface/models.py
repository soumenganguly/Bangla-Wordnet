from django.db import models
from django import forms

# Create your models here.

class Search(forms.Form):
    word=forms.CharField(max_length=20)

