# Django imports
from django.shortcuts import get_object_or_404

# Rest framework imports
from rest_framework import generics, viewsets
from rest_framework import serializers

# Local imports
from .models import Comment, Company, Item
from .serializers import CommentSerializer, CompanySerializer, ItemSerializer


# Item views
class ItemVS(viewsets.ModelViewSet):
    """ViewSet for Item model"""

    queryset = Item.objects.filter(active=True)
    serializer_class = ItemSerializer


# Company views
class CompanyVS(viewsets.ModelViewSet):
    """ViewSet for Company model"""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# Comment views
class CommentVS(viewsets.ModelViewSet):
    """ViewSet for Comment model"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreate(generics.CreateAPIView):
    """API view for creating a comment"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(item=self.kwargs["pk"])

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        item = get_object_or_404(Item, pk=pk)
        comment_qs = Comment.objects.filter(item=item, comment_user=self.request.user)
        if comment_qs.exists():
            raise serializers.ValidationError("You have already commented on this item")
        serializer.save(comment_user=self.request.user, item=item)


class CommentList(generics.ListAPIView):
    """API view for listing comments of an specific item"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(item=self.kwargs["pk"])
