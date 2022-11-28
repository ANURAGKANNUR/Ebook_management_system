from rest_framework import serializers
from .models import Genre, Ebook, Rating

class RatingSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Rating
        fields='__all__'
class Ratingviewserializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Rating
        exclude=('id','favourite','ebook')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'
class EbookSerializer(serializers.ModelSerializer):
    createdby=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Ebook
        fields='__all__'



class EbookListSerializer(serializers.ModelSerializer):
    rating=Ratingviewserializer(many=True,read_only=True)
    category=serializers.StringRelatedField()
    class Meta:
        model=Ebook
        exclude=('createdby',)

class EbookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ebook
        exclude=('id','createdby')
class RatingSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Rating
        exclude=('ebook',)