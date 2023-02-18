from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name='hompage'),
    path('insert/', insert,name='inspro'),
    path('update/', update,name='uppro'),
    path('delete/', delete,name='delpro'),
    path('list/', listp,name='lipro'),
]