from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import typing
from .models import Book
from authentication.models import Token

def book_serialiser(book:Book):
    return{
        "id": book.id,
        "title": book.title,
        "content": book.content,
        'author': book.author.name
    }

@api_view(['get'])
def getbooks(request:Request):
    books_list= [
        book_serialiser(book)

        for book in Book.objects.all()
    ]
    return Response(books_list)

@api_view(['post'])
def addBook(request: Request):
    body= typing.cast(dict,request.data)
    title = body.get("title")
    content = body.get("content")
    auth_token = request._request.META.get('HTTP_AUTHORIZATION')
    if (not auth_token):
        return Response({
            'error':"user not found"
        },
        status=404
        )
    user= Token.objects.get(key=auth_token)
    book= Book.objects.create(title=title,content=content,author=user.user)
    return Response(book_serialiser(book))
