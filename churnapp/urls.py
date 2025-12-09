from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('login/',views.loginpage,name='login'),
   path('register/',views.registerpage,name='register'),
   path('main/',views.main,name='main'),
   path('switchpage/', views.switchpage, name='switchpage'),
   path('conpro/', views.conpro, name='conpro'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('churn/',views.churn,name='churn'),
   path('get_user_details/', views.get_user_details, name='get_user_details'),
   
   

]