from django.urls.conf import path
from tracker import views

app_name = "tracker"

urlpatterns = [
    path('', views.TrackerListView.as_view(), name='home'),
]