from django.urls import path
from.import views
from.import feed

urlpatterns = [
    
    path('',views.index,name='homepage'),
    path('xyz/',views.test),
    path('login/',views.login,name="loginpage"),
    
    path('register/',views.register,name='registerpage'),
    path('logout/',views.logout),
    path('feed/',feed.latest()),
    path('search/',views.search),
    path('search/searchsub/',views.schsub),
    
    
]