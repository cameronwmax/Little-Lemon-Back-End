from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.http import HttpResponse

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]

# class bookingView(APIView):
  
#   def get(self, request):
#     items = Booking.objects.all()
#     serializer = BookingSerializer(items, many=True)
#     return Response(serializer.data)
  
#   def post(self, request):
#     serializer = BookingSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response({"status": "success", "data": serializer.data})


# class menuView(APIView):
  
#   def get(self, request):
#     items = Menu.objects.all()
#     serializer = MenuSerializer(items, many=True)
#     return Response(serializer.data)
  
#   def post(self, request):
#     serializer = MenuSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response({"status": "success", "data": serializer.data})


def index(request):
  return render(request, 'index.html', {})


# def sayHello(request):
#   return HttpResponse("Hello World!")
