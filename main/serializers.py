from rest_framework import serializers

from .models import Item, Company, Comment


class CommentSerializer(serializers.ModelSerializer):
    comment_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"
