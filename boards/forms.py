from django import forms
from .models import Topics

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget = forms.Textarea(
            attrs={'row':5,'placeholder':'what is in your mind'}
        ),
        max_length=4000,
        help_text = 'The max length of the text is 4000.'
    )

    class Meta:
        model = Topics
        fields = ['subject','message']