from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        widgets = {
            'rating': forms.RadioSelect(
                choices=[(i, str(i)) for i in range(1, 6)],
                attrs={'class': 'inline-radio'}
            )
        }
