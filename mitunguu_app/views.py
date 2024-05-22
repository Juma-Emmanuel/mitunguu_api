from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
class UserRegistrationView(generics.CreateAPIView):
   
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
       
        return Response({}, status=status.HTTP_201_CREATED)
class UsersView(APIView):    

    def get(self, request):
        
        users = User.objects.filter(is_staff=False)
        
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data ,status=status.HTTP_200_OK)
    def perform_create(self, serializer):
        return serializer.save()

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
       
        user = request.user

        

        serializer = UserSerializer(user)

       
        return Response(serializer.data)
class CreateProductView(generics.CreateAPIView):
    
    serializer_class = ProductCreateSerializer
    # permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"message": "Product Ad posted successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user=request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({
            'message': 'Product created successfully',
            'product': serializer.data
            }, status=status.HTTP_201_CREATED,)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetProductView(APIView):
    # permission_classes = [IsAuthenticated]    

    def get(self, request):
        
        products = Product.objects.all()
        serializer = ProductViewSerializer(products, many= True)
        return Response(serializer.data ,status=status.HTTP_200_OK)