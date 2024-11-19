from django import forms
from .models import Comment



class StoryCommentFormModel(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

        labels = {
            'message' : 'Message'
        }

        widgets = {
            'message' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 7,
                    'placeholder' :"Write your message"
                }
            ),
        }