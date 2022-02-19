from django.urls import path, re_path
from . import views as v


urlpatterns = [
    path('', v.index, name='index'),
    path('req/', v.request, name='req'),
    path('news/', v.news, name='news'),
]