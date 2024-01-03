
from django.urls import path
from .views import *


urlpatterns = [
    path('contact_api/',ContactList.as_view(),name='contact_api'),
    path('product_api/',ProductList.as_view(),name='product_api'),
    path('combined_api/',CombinedList.as_view(),name='combined_api'),
    path('subscriber/',SubsciberApiView.as_view(),name='subscriber'),
]
