"""
URL configuration for socialproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", status=200)

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('health/', health_check, name='health_check'),  # Health check endpoint
    path('', redirect_to_login, name='home'),  # This will redirect root URL to login
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
