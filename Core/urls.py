
from django.urls import path

from .views import about, changepassword, contact, create, forgetpassword,index,  recipe, reset_password, single,  subscribers, userprofile

urlpatterns = [
    
    
    path('about_list/',about,name='about_list'),
    path('contact/', contact, name='contact'),
    path('create/',create,name='create'),
    path('subscribers/',subscribers,name='subscribers'),
    path('',index,name='index_lists'),
    path('single/',single,name='single'),
    path('userprofile/',userprofile,name='userprofile'),
    path('recipes_list/',recipe,name='recipes_list'),
    path('changepassword/',changepassword,name='changepassword'),
    path('forgetpassword/',forgetpassword,name='forgetpassword'),
    path('rst_password/',reset_password,name='rst_password'), 
]

