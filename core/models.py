from datetime import date

from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

colors=(
    ('red','Red'),
    ('yellow','Yellow'),
    ('blue','Blue'),
    ('white','White'),
    ('black','Black'),
    ('green','Green'),
    ('orange','Orange'),
)

class BaseModel(models.Model):

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Contact(BaseModel):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    # message=models.TextField()

    def __str__(self):
        return self.name

class Category(BaseModel):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
class Type(BaseModel):
    name=models.CharField(max_length=50, null=True , blank=True)


    def __str__(self):
        return self.name

class Product(BaseModel):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=RichTextField(blank=False,null=False)
    discount=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    views=models.IntegerField(default=0)
    image=models.ImageField(upload_to=True,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    type=models.ForeignKey(Type,on_delete=models.CASCADE,null=True)
    color=models.CharField(max_length=50,choices=colors)
    active=models.BooleanField(default=True)
    slug=models.SlugField(null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(f"{self.name}")
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    
class About(BaseModel):
    name=models.CharField(max_length=50)
    description=RichTextField(blank=False,null=False)
    
    def __str__(self):
        return self.name
    
class Blog(BaseModel):
    name=models.CharField(max_length=50)
    description=RichTextField(blank=False,null=False)
    likes=models.IntegerField(default=0)
    views=models.IntegerField(default=0)
    image=models.ImageField(upload_to=True,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    type=models.ForeignKey(Type,on_delete=models.CASCADE,null=True)
    active=models.BooleanField(default=True)
    slug=models.SlugField(null=True,blank=True)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(f"{self.name}")
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name

    # def __save__(self,*args,**kvargs):
        
    #     if not self.pk:
    #         print('create')
    #     else:
    #         print('update')
    #     print('create or update')

    #     super().save(*args,**kvargs)

    @property
    def price_after_discount(self):
        return self.price-self.price*self.discount/100

class Settings(BaseModel):
    instagram=models.URLField(max_length=50)
    facebook=models.URLField(max_length=50)
    google=models.URLField(max_length=50)
    linkedin=models.URLField(max_length=50)

    def __str__(self):
        return self.instagram

class Logo(BaseModel):

    logo=models.ImageField(max_length=50)

    def __str__(self):
        return self.logo
    
class Subscriber(BaseModel):
    email=models.EmailField(unique=True)
    
    def _str_(self):
        return self.email        
    
