from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from core.api.serializers import *
from core.models import *

class ContactList(generics.ListCreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    
class ProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class CombinedList(APIView):
    def get(self,request,format=None):
        context={"request":request}
        
        products=Product.objects.all()
        contacts=Contact.objects.all()
    
        product_serializer=ProductSerializer(products ,many=True , context=context)
        contact_serializer=ContactSerializer(contacts, mant=True ,context=context)
    
        data= [
            product_serializer.data,
            contact_serializer.data,  
        ]
    
        return Response(data, status=status.HTTP_200_Ok)
    
    # class SubscriberList(generics.ListCreateAPIView):
    #     queryset=Subscriber.objects.all()
    #     serializer_class=SubscriberSerializer
    
class SubsciberApiView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SubscriberSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)