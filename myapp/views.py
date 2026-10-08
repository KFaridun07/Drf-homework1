from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Author, Book,Country
from .serializer import AuthorSerializer, BookSerializer,CountrySerializer


@api_view(['GET'])
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error': 'Not found'},status=404)

    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['PUT'])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error': 'Not found'},status=404)

    serializer = BookSerializer(book,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response( {'error': 'Not found'}, status=404)

    book.delete()

    return Response(status=204)

@api_view(['GET'])
def get_countrys(request):
    countrys = Country.objects.all()
    serializer = CountrySerializer(countrys, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_country(request):
    serializer = CountrySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

