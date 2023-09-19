from django.urls import include, path
from .import views
from .import api




urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.new_register,name='new_register'),
    path('login',views.new_login,name='new_login'),
    path('header',views.header,name='header'),
    path('navbar',views.navbar,name='navbar'),
    path('api/list',api.registerapi,name='registerapi'),
     path('api/list/<int:id>/',api.lgoicl,name='lgoicl'),
    
]
