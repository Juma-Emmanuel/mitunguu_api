from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
class UserRegistrationSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()
    email = serializers.CharField()
    class Meta:
        model = User        
        fields =fields = '__all__'        

    def create(self, validated_data):
        user_data = { 
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            
            'username': validated_data['email'],         
            'email': validated_data['email'],
            'password': validated_data['password'],
        }
              
        return User.objects.create_user(**user_data)
class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id', 'username', 'email', 'first_name', 'last_name']
class ProductCreateSerializer (serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'location', 'mobile']

class ProductViewSerializer (serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = '__all__'