
from django.urls import path

from .views import  about, contact, create, index,  recipe, send_email_view, single, LatestStoryListView, userprofile

urlpatterns = [
    
    
    path('about_list/',about,name='about_list'),
    path('contact/', contact, name='contact'),
    path('create/',create,name='create'),
    path('send-emails/', send_email_view, name='send_email_view'),
    path('',index,name='index_lists'),
    path('',LatestStoryListView.as_view() , name='index_lists'),
    path('single/',single,name='single'),
    path('userprofile/',userprofile,name='userprofile'),
    path('recipes_list/',recipe,name='recipes_list'),
    
]

