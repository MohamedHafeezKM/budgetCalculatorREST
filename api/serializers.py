from rest_framework import serializers

from django.contrib.auth.models import User

from api.models import Transaction


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']

        read_only_fields=['id']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    

class TransctionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields='__all__'
        read_only_fields=['id','user']



