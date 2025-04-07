from rest_framework import serializers

from .models import Item, Company


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"
