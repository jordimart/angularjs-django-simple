from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'country', 'province', 'city')

    def create(self, validated_data):

        return Restaurant.objects.create(**validated_data)

    def update(self,instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('name', instance.name)
        instance.province = validated_data.get('name', instance.name)
        instance.city = validated_data.get('name', instance.name)
        instance.save()
        return instance