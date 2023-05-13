from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm, ClearableFileInput
from .models import Post, Comment, Tag
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

    
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags", "series", "contributors"]

    files = forms.FileField(
        widget=ClearableFileInput(attrs={"multiple": True}), required=False
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(PostForm, self).__init__(*args, **kwargs)
        if self.user:
            # Exclude the current user from the list of contributors
            self.fields["contributors"].queryset = get_user_model().objects.exclude(
                id=self.user.id
            )

        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["tags"].widget.attrs.update({"class": "form-control"})
        self.fields["series"].widget.attrs.update({"class": "form-control"})
        self.fields["contributors"].widget.attrs.update({"class": "form-control"})

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

# Define a form class to be used for ReplyCommentCreateView
class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "comment_detail",
            "commenter",
        )

    def __init__(self, *args, pk=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-8'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))



    # Clean the form to assign the parent comment and post to the reply comment
    def clean(self):
        
        # Get the comment to be created
        cleaned_data = super().clean()
        instance = self.instance

        # Get the pk kwargs from the url
        pk = self.pk

        # Assign the parent comment to the instance
        instance.parent = get_object_or_404(Comment, pk=pk)

        # Assign the post to the instance
        instance.post = instance.parent.post

        # Done
        return cleaned_data



class generalErrorMixin:
    def clean(self):
        # Check if any field has an error
        if self.errors:
            raise forms.ValidationError("Please fix the errors below and try again")
        
class TagCreateForm(generalErrorMixin, forms.ModelForm):

    class Meta:
        model = Tag
        fields = (
            "name",
        )

    def clean_name(self):
        super().clean()
        name = self.cleaned_data['name']
        matching_tags = Tag.objects.filter(name__iexact=name)

        error_collection = []

        if matching_tags.exists():
            # The name matches a record in the database
            # You can raise a validation error or perform further actions as needed
            error_collection.append("Tag name already exists.")

        if error_collection:
            raise forms.ValidationError(error_collection)
        
        return name