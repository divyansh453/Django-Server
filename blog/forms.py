from django.db import models
from django.forms import fields
from .models import Post
from django import forms
from django.contrib.auth.forms import UserCreationForm


class Post_create_form(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','content','image']