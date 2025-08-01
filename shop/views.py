from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from .models import Product, Order
from .serializers import UserSerializer, LoginSerializer, OrderSerializer, OrderHistorySerializer, ProductSerializer
from django.contrib.auth import login

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({"message": "Login successful", "user": user.username})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin:
            return Response({"error": "Only admin users can add products."}, status=403)
        return super().post(request, *args, **kwargs)

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}
class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')



@login_required
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


