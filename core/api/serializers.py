from core.models import Contact,Product,Category,Subscriber
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=('name','email','subject')
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','name')
        
        
class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Product
        fields=('name','price','description','likes','category')
        
class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subscriber
        fields=['email', ]