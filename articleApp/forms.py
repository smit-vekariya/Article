from tkinter import Widget
from turtle import title
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=250)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2',]

class ArticleForm(forms.ModelForm):
    articletag=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}))
    class Meta:
        model=Article
        fields=['title','content','image','draft','articletag']
       
class ArticleUpdateForm(forms.ModelForm):
    articletag=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}))
    class Meta:
        model=Article
        fields=['title','content','image','draft','articletag',]
    
       