"""carpool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.shortcuts import redirect

from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', lambda request: redirect('/login/')),
    path('admin/', admin.site.urls),
    path('login/' , include('logPage.urls')),
    path('rider/', include('rider.urls')),
    path('driver/' , include('driver.urls'))
]
