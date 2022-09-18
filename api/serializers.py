from rest_framework import serializers
from db.models import *


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'email', 'name', 'password')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('title',)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'file', 'created_at', 'restaurant')


class ResultSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(read_only=True)

    class Meta:
        model = Menu
        fields = [
            'file',
            'restaurant',
            'total_votes',
            'created_at'
        ]