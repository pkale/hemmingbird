from rest_framework import serializers
from .models import Songs, Customer, Tailor, Order


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("name", "gender", "height", "sleeve_length", "waist_length","shoulder_length", "shirt_size")

class TailorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tailor
        fields = ("name", "location", "capacity")

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("customer_name", "order_number", "item", "color","fabric", "order_time")

