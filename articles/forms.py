from django import forms

from .models import Comment

# ModelForm is a helper class designed to translate database models into forms. We can use it to create a form
# called appropriately enough, CommentForm. 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ("comment",)

