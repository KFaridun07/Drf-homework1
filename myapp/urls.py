from django.urls import path
from .views import *

urlpatterns = [
    path('authors',get_authors),
    path('create/author',create_author),
    path('books',get_books),
    path('create/book',create_book),
    path('book/<int:pk>',get_book),
    path('update/book/<int:pk>',update_book),
    path('delete/book/<int:pk>',delete_book),
    path('countries',get_countrys),
    path('create/country',create_country),
]
