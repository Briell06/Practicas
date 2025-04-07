from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        extra_kwargs = {
            'name': {
                'min_length': 2,
                'error_messages': {
                    'min_length': 'Name must be at least 2 characters long.'
                }
            }
        }
