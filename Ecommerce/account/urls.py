from django.urls import path
from .views import *
from product.views import *
urlpatterns = [
    path('home/',home),
    path('login/', login,name='acclogin'),
    path('register/', register,name='accreg'),

]