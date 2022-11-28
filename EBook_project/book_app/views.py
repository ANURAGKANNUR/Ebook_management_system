from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre, Ebook, Rating
from .permissions import CreatedUseronly,ReviewUseronly
from .serializers import CategorySerializer,EbookSerializer,EbookUpdateSerializer,EbookListSerializer,RatingSerializer
# Create your views here.


# to create categories
class CategoryCreateClass(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Genre.objects.all()
    serializer_class = CategorySerializer

# to view list of categories
class CategoryList(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Genre.objects.all()
    serializer_class = CategorySerializer

#to update/delete category
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = CategorySerializer

#to create the Ebook
class CreateEbook(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    def perform_create(self, serializer):
        # pk = serializer.
        serializer.save(createdby=self.request.user)

#list view of ebook(for Authenticated user only)
class EbookList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ebook.objects.all()
    serializer_class = EbookListSerializer

#detail view of ebook (for Authnticated users)
class EbookDetail(generics.RetrieveAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookListSerializer

#to retrive and update the Ebook (only for created users)
class EbookUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [CreatedUseronly]
    queryset = Ebook.objects.all()
    serializer_class = EbookUpdateSerializer

#to retrive and delete ebook
class EbookDelete(generics.DestroyAPIView):
    permission_classes = [CreatedUseronly]
    queryset = Ebook.objects.all()
    serializer_class = EbookUpdateSerializer


class RatingCreate(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Rating.objects.all()
    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        ebook=Ebook.objects.get(pk=pk)

        rating_user=self.request.user
        rating_queryset=Rating.objects.filter(ebook=ebook,review_user=rating_user)
        if rating_queryset.exists():
            raise ValidationError("You Already reviewed the ebook!!!!")

        serializer.save(ebook=ebook,review_user=rating_user)

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [ReviewUseronly]
