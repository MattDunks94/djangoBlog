from .models import Comment
from django import forms


# Creating our comment section form.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # The comma, at the end, is important!
        # Python reads it as a tuple instead of a string.
        fields = ('body',)
