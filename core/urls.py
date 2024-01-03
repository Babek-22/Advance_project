from django.urls import path

from core.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('blog/',blog,name='blog'),
    path('contact/',contact,name='contact'),
    # path('login/',login,name='login'),
    path('checkout/',checkout,name='checkout'),
    path('confirmation/',confirmation,name='confirmation'),
    path('product/',product_list,name='product_list'),
    # path('product_list',ProductList.as_view(),name='products'),
    path('cart/',cart,name='cart'),
    path('elements/',elements,name='elements'),
    path('single_blog/',single_blog,name='single-blog'),
    # path('product/<slug:slug>/',single_product,name='single-product'),
    path('product/<slug:slug>/',ProductDetail.as_view(),name='single-product'),
    path('search/', search, name='search'),
    
       
]