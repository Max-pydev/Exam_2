from django.urls import path
from book.views import home_view

urlpatterns=[
    path('', home_view, name='home')
]