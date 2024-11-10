from typing import Any
from django import forms
from .models import Post , Commants

class PostForm(forms.ModelForm):
    class Meta():
        model = Post # this is connected to the models 
        fields = ['title' ,'category' , 'body'  , 'status'] # this is fields from comite 
"""
we dont learn auth from django and we have to create a simple user comments 
"""
class CommentForm(forms.ModelForm):
    class Meta():
        model = Commants # this is from commments 
        fields = ['TEXT']
# this is 
# mekanism shygra ro bebinam 
class CreateCAtegory(forms.Form):
    name_category = forms.CharField()
    

class SearchPostForm(forms.Form):
    values = forms.CharField(max_length=180)
    
# hamin alan # a
class SignForms(forms.Form): # i dont want to usemodels forms from this  
    username = forms.CharField(max_length=150 , label="Username")
    password = forms.CharField(max_length=150 , label="password")
    confermation = forms.CharField(max_length=100 , label='Confermation')
    # this is the baseic validatro in forms 
    def clean_confermation(self):
        if self.cleaned_data.get('password') == self.cleaned_data.get('confermation'):
            return self.cleaned_data.get('confermation')
        else : 
            raise forms.ValidationError('the password is not match')