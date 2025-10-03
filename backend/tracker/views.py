from django.shortcuts import render
from tracker.models import Media
from django.views.generic.base import View

class TrackerListView(View):
    """
    Display a list of all media items in the tracker.
    
    This view retrieves all Media objects from the database and
    renders them in a list format for the user to browse.
    """
    def get(self, request, *args, **kwargs):
        media = Media.objects.all()
        context = { 'media': media, } # Dictionary to pass data to the template
        return render(request, 'tracker/media_list.html', context)