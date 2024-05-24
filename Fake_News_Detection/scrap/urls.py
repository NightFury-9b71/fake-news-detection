from django.urls import re_path
from . import views

urlpatterns=[
    re_path('news/',views.getScrap, name='getScrap'),
    re_path('show/',views.showNews,name='showNews'),
    re_path('delete/',views.delete, name='delete'),

]