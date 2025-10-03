from django.shortcuts import render, get_object_or_404
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


class MediaEditView(View):
    """
    Handle editing of existing media items.
    
    GET: Display a MediaForm pre-filled with the media's current data.
    POST: Process form submission and update media in database.
    """
    def get(self, request, pk, *args, **kwargs):
        media = get_object_or_404(Media, pk=pk)
        form = MediaForm(instance=media)
        context = { 'form': form, 'media': media, }
        return render(request, "tracker/edit_media.html", context)

    def post(self, request, pk, *args, **kwargs):
        media = get_object_or_404(Media, pk=pk)
        form = MediaForm(request.POST, instance=media)
        if form.is_valid():
            media = form.save()
            media.save()
            return HttpResponseRedirect(reverse_lazy("tracker:home"))


class MediaDeleteView(View):
    """
    Handle deletion of media items.
    
    GET: Display confirmation page for media deletion.
    POST: Delete the specified media item from the database.
    """
    def get(self, request, pk, *args, **kwargs):
        media = Media.objects.get(pk=pk)
        context = { 'media': media, }
        return render(request, 'tracker/delete_media.html', context)

    def post(self, request, pk, *args, **kwargs):
        media = Media.objects.get(pk=pk)
        media.delete()
        return HttpResponseRedirect(reverse_lazy("tracker:home"))