from django.urls import path
from .views import *
urlpatterns = [
    #path('', home,name='hompage'),
    path('insertcat/', insertcat,name='inscat'),
    path('updatecat/', updatecat,name='upcat'),
    path('deletecat/', deletecat,name='delcat'),
    path('listcat/', listcat,name='licat'),
]