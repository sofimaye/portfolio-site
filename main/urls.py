
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page, name='home'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('contacts',views.contacts, name='contacts'),
]
