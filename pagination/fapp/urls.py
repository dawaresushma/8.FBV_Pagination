from django.urls import path,include
from .views import pagination

urlpatterns = [
    path('',pagination,name='books')
]