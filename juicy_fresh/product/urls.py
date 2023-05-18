from django.urls import path
from . import views


urlpatterns=[
    path('',views.about2,name='pro'),
    path('cmt/',views.cmt),
    path('like/',views.like),
    path('autoc/',views.autoc,name='autocmplt'),
    




]