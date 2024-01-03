from typing import Any
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse 
from core.models import *
from core.forms import ContactForm
from django.views.generic import ListView,DetailView
from django.db.models import Q
from django.utils.dateparse import parse_date

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    context={
        'about': About.objects.all()
    }
    return render (request,'about.html',context)

def blog(request):
    
    userinput = request.GET.get('inputname', '')  # Get 'inputname' parameter or default to empty string
    userinput_list = userinput.split(' ')  # Split the input into a list of words
   
    startdate_str=request.GET.get('startdate','')    
    enddate_str=request.GET.get('enddate','')
    startdate=parse_date(startdate_str) if startdate_str else None
    enddate=parse_date(enddate_str) if enddate_str else None
    
    
    category_id=request.GET.getlist('category','')
    
    if startdate and enddate:
        query &=Q(created_at__date__gte=startdate) & Q(created_at__date__gte=enddate)
        
    query = Q(active=True)
   
    blog=Blog.objects.all()
    category=Category.objects.all()
    type=Type.objects.all()
    
    if 'type' in request.GET.keys():
        blog=Blog.objects.filter(
            type_id__name=request.GET['type']
        )    
        
    context= {
            'blog':blog[0:2:1],
            'categories':category,
            'count':blog.count(),
            'userinput':userinput,
            'type':type           
            }
    
    return render(request,'blog.html',context)


def contact(request):
    context ={
        'contact': ContactForm()
    }
    if request.method == 'POST':
        result=ContactForm(request.POST)
        if result.is_valid():
            result.save()
            HttpResponseRedirect(reverse('home'))
        else:
            print(result.errors)
    return render(request,'contact.html',context)


def login(request):
    return render(request,'login.html')

def checkout(request):
    return render(request,'checkout.html')

def confirmation(request):
    return render(request,'confirmation.html')

def product_list(request):
 
    
    
    
    products=Product.objects.all()
    category=Category.objects.all()
    type=Type.objects.all()
    
    if 'type' in request.GET.keys():
        products=Product.objects.filter(
            type_id__name=request.GET['type']
        )    
    
    if 'category' in request.GET.keys():
        products=Product.objects.filter(
            category_id__name=request.GET['category']
        )    
        
    context= {
            'products':products,
            'category':category,
            'count':products.count(),
            'type':type           
            }
    return render(request,'product_list.html',context)

# class ProductList(ListView):
#     model=Product
#     template_name='product_list.html'
#     context_object_name='products'
#     ordering=['created_at']
#     paginate_by=3
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["categories"] = Category.objects.all()
#         context['count']=Product.objects.filter(active=True).count()
#         return context
#     def get_paginate_by(self,queryset):
#         return self.request.Get.get('paginate_by',self.paginate_by)
        
    
    
    
    
def single_product(request, slug):
    context={
        'product':Product.objects.get(slug=slug)
    }
    return render(request,'single-product.html',context)

class ProductDetail(DetailView):
    model=Product
    template_name='single-product.html'
    context_object_name='single-product'
    slug_url_kwarg='slug'
    slug_field='slug'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        return context
    
    
def cart(request):
    return render(request,'cart.html')

def elements(request):
    return render(request,'elements.html')

def single_blog(request):
    return render(request,'single-blog.html')

# def single_product(request):
#     return render(request,'single-product.html')

def search(request):
    
    query = request.GET.get('query')

    if query:
        products = Product.objects.filter(name__icontains=query)
        # course = Course.objects.filter(title__icontains=query)
        context = {
            'title': 'Search',
            'query': query,
            'products': products,
            # 'course': course,
        }
        return render(request, 'search.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))



