from django.urls import path
from travelapp import views

urlpatterns = [
    path('', views.new, name='new'),
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
