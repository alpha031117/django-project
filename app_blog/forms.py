from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm, ClearableFileInput
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'series', 'contributors']
    
    files = forms.FileField(widget=ClearableFileInput(attrs={'multiple': True}), required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if self.user:
            # Exclude the current user from the list of contributors
            self.fields['contributors'].queryset = get_user_model().objects.exclude(id=self.user.id)

        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs.update({'class': 'form-control'})
        self.fields['series'].widget.attrs.update({'class': 'form-control'})
        self.fields['contributors'].widget.attrs.update({'class': 'form-control'})