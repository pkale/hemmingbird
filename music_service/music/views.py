#from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Songs, Customer, Tailor, Order
from .serializers import SongsSerializer, CustomerSerializer, TailorSerializer, OrderSerializer


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

class ListCustomersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ListTailorsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Tailor.objects.all()
    serializer_class = TailorSerializer

class ListOrdersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer