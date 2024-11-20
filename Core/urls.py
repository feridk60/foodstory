
from django.urls import path

from .views import  about, contact, create, index,  recipe, single, LatestStoryListView,  subscribers, userprofile

urlpatterns = [
    
    
    path('about_list/',about,name='about_list'),
    path('contact/', contact, name='contact'),
    path('create/',create,name='create'),
    path('subscribers/',subscribers,name='subscribers'),
    path('',index,name='index_lists'),
    path('',LatestStoryListView.as_view() , name='index_lists'),
    path('single/',single,name='single'),
    path('userprofile/',userprofile,name='userprofile'),
    path('recipes_list/',recipe,name='recipes_list'),
    
]

