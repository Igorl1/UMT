from django.shortcuts import render
from tracker.models import Media
from django.views.generic.base import View
from tracker.forms import MediaForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

class MediaListView(View):
    """
    Display a list of all media items in the tracker.
    
    This view retrieves all Media objects from the database and
    renders them in a list format for the user to browse.
    """
    def get(self, request, *args, **kwargs):
        media = Media.objects.all()
        context = { 'media': media, } # Dictionary to pass data to the template
        return render(request, 'tracker/media_list.html', context)


class MediaAddView(View):
    """
    Handle creation of new media items.
    
    GET: Display an empty MediaForm for user input.
    POST: Process form submission and save new media to database.
    """
    def get(self, request, *args, **kwargs):
        context = { 'form': MediaForm(), }
        return render(request, "tracker/add_media.html", context)

    def post(self, request, *args, **kwargs):
        form = MediaForm(request.POST)
        if form.is_valid():
            media = form.save()
            media.save()
            return HttpResponseRedirect(reverse_lazy("tracker:home"))