from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import serializers

from api.serializers import RegisterUserSerializer,TransctionSerializer
from api.models import Transaction

# Create your views here.

class SignUpView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        


class TransactionView(ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransctionSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        qs=self.queryset.filter(user=self.request.user)
      
        return qs
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        logged_user=self.request.user
        owner=self.get_object().user
        print(owner,'i')
        if logged_user==owner:
            return super().perform_update(serializer)
        else:
            raise serializers.ValidationError('Owner Permission required')
        
    def perform_destroy(self, serializer):
        logged_user=self.request.user
        owner=self.get_object().user
        print(owner,'i')
        if logged_user==owner:
            return super().perform_destroy(serializer)
        else:
            raise serializers.ValidationError('Owner Permission required')
        
        
        


