from django import forms
from tracker.models import Media

class MediaForm(forms.ModelForm):
    """
    Form for Media model CRUD operations.
    """
    class Meta:
        model = Media
        fields = ['title', 'status', 'rating', 'type', 'description']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }