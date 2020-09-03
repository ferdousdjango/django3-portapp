from django.urls import path,include
from . import views



urlpatterns = [
    
   
    path('', views.webapp, name='webapp'),
    path('password/', views.password_generator, name='password_generator'),

   
]