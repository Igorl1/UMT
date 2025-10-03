"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from accounts import views as accounts_views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.HomeView, name='home'),
    path('tracker/', include('tracker.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("registration/", accounts_views.RegistrationView, name="registration"),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', accounts_views.LogoutConfirmView, name='logout'),
]
