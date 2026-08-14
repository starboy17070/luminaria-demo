
from django.contrib import admin
from django.urls import path

from english.views import luminaria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', luminaria)
]
