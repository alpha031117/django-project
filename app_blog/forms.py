from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm, ClearableFileInput
from .models import Post, Comment
from django.shortcuts import get_object_or_404

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
