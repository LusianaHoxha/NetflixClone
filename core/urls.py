from django.urls import re_path
from .views import Home

app_name='core'
urlpatterns = [
    re_path('',Home.as_view())
]