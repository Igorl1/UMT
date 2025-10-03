from django.urls.conf import path
from tracker import views

app_name = "tracker"

urlpatterns = [
    path('', views.MediaListView.as_view(), name='home'),
    path('add/', views.MediaAddView.as_view(), name='add_media'),
]