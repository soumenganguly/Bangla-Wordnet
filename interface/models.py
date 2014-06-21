from mongoengine import *
from django import forms

# Create your models here.

class Search(forms.Form):
    word=forms.CharField(max_length=20)

class Synset(Document):
    word=StringField(max_length=200)
    cat=StringField(max_length=200)
    concept=StringField(max_length=200)
    synset=ListField(StringField(max_length=200))
    example=StringField(max_length=200)
