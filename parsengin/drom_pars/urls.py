from django.urls import path
from .views import *

urlpatterns = [
    path('', Parsing.as_view(), name='main_url'),
    path('info/<id>/', ParsMore.as_view(), name='main_info_url')
]