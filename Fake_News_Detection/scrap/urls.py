from django.urls import re_path
from . import views

urlpatterns=[
    re_path('',views.getScrap, name='getScrap'),
    re_path('show',views.showNews,name='showNews'),
]