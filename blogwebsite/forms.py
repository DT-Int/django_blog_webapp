from django import forms
from . models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your title here'}),
			'author': forms.Select(attrs={'class': 'form-control', 'placeholder':'Choose who the blogger is'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Enter your post here'}),
		}

