from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI


api = NinjaAPI()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),

    # Applications route
    path("auth/", include("applications.authentication.urls"))
]
