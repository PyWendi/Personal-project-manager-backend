"""
URL configuration for PersonalProjectManager project.

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
from django.urls import path, include
from django.http import HttpResponse
from ninja import NinjaAPI

# Importing route

api = NinjaAPI()

@api.get("/add/{a}/{b}")
def add (request, a:int, b:int):
    return {"result": a + b}
    # return HttpResponse({"result": a + b})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    # path("api/", api.urls),
    path("auth/", include("applications.authentication.urls"))
]
