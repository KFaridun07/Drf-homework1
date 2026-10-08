from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country',
        write_only=True
    )

    class Meta:
        model = Author
        fields = ['id', 'name', 'age', 'country', 'country_id']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only = True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all(),
        source = 'author',
        write_only = True
    )

    title_upper = serializers.SerializerMethodField()
    is_expensive = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title','pages','price','author','author_id','title_upper','is_expensive']

    def validate_title(self,data):
        if not data[0].isupper():
            raise serializers.ValidationError('Title must be start with a capital letter')
        return data


    def validate(self,data):
        if data['price'] <=0:
            raise serializers.ValidationError('Price must be greater 0')

        if data['pages'] > 1000 and data['price'] < 200:
            raise serializers.ValidationError('Takaya kniga ne mojet stoit menshe 200')

        return data

    def get_title_upper(self,obj):
        return obj.title.upper()

    def get_is_expensive(self,obj):
        return obj.price > 200

    def to_representation(self, instance):
        data =  super().to_representation(instance)

        data['book_info'] = f'{instance.title} - {instance.pages} pages'

        return data
    