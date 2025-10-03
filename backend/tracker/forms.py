from django import forms
from tracker.models import Media

class MediaForm(forms.ModelForm):
    """
    Form for Media model CRUD operations.
    """
    class Meta:
        model = Media
        fields = ['title', 'status', 'rating', 'genre', 'description']