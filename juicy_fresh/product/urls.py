from django.urls import path
from . import views


urlpatterns=[
    path('',views.about,name='pro'),
    path('cmt/',views.cmt),
    path('like/',views.like),




]