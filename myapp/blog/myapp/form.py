from dataclasses import fields
from django import forms
from myapp.models import *




class YorumForm(forms.ModelForm):

    class Meta:

        model = YorumModel

        fields = ('yorum', )




class YaziForm(forms.ModelForm):

    class Meta:

        model = UrunModel

        exclude = ('yazar', 'olusturma', 'degistirma', 'slug')