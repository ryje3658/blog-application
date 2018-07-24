from django import forms
from django.forms import ModelForm
from .models import Contact, Post, Category
from django.forms import BaseModelFormSet
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ContactForm(forms.ModelForm):

	"""Contact Me form on Contact page."""
	
	class Meta:
		model = Contact
		fields = ['name', 'email', 'message']
		widgets = {
			'name' : forms.TextInput(attrs={'placeholder':'Josh Smith', 'class':"form-control"}),
			'email' : forms.EmailInput(attrs={'placeholder': 'email@gmail.com','class':"form-control"}),
			'message' : forms.Textarea(attrs={'placeholder': 'Please type message here.','class':"form-control",}),
		}

class BaseCreatePostFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Category.objects.all()

class CreatePostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'body','category','image']
		field_classes = {
            'category': forms.ModelChoiceField,
        }
		widgets = {
			'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
			'body': CKEditorUploadingWidget(),
			'category': forms.Select(),
			'image': forms.ClearableFileInput(),
		}