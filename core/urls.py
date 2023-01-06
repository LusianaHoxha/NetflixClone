from django.urls import re_path
from core.views import Home, ProfileList, ProfileCreate,Watch,ShowMovieDetail,ShowMovie

app_name='core'

urlpatterns = [
    re_path('',Home.as_view()),
    re_path('profile/',ProfileList.as_view(),name='profile_list'),
    re_path('profile/create/',ProfileCreate.as_view(),name='profile_create'),
    re_path('watch/<str:profile_id>/',Watch.as_view(),name='watch'),
    re_path('movie/detail/<str:movie_id>/',ShowMovieDetail.as_view(),name='show_det'),
    re_path('movie/play/<str:movie_id>/',ShowMovie.as_view(),name='play')
]