from django import forms
from django.db import models
from .models import Post

# class PostForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         fields = ['name', 'phone']
#     # class Meta:
#     #     model = Post
#     #     fields = ('name', 'phone','color','size')
#
from django import forms
from django.shortcuts import render

# class ContactForm(forms.Form):
#       name = forms.CharField(required=False)
#       email = forms.EmailField(label='Your email')
#       comment = forms.CharField(widget=forms.Textarea)

# from django import forms
#
# class EmailPostForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     email = forms.EmailField()
#     to = forms.EmailField()
#     comments = forms.CharField(required=False,
#                                widget=forms.Textarea)