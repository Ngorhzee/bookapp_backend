from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import typing
from . import models

@api_view(['post'])
def signup(request:Request):
    body= typing.cast(dict,request.data)
    email= body.get("email")
    name=body.get("name")
    password= body.get("password")
    user = models.User(email=email,name=name)
    password= user.set_password(password)
    user.save()
    return Response({
        "email": email,
        "name":user.name
    })

@api_view(['post'])
def login(request:Request):
    body= typing.cast(dict,request.data)
    email=body.get("email")
    password=body.get("password")

    try:
        user=models.User.objects.get(email=email)
    except models.User.DoesNotExist:
        return Response({
            "error":"User does not exist"
        },status=404)
    if not user.check_password(password):
        return Response({
            "error":"password incorrect"
        }, status=401)
    try:
        token=models.Token.objects.get(user=user)
    except models.Token.DoesNotExist:
        token=models.Token.objects.create(user=user)
    return Response({
        "token": token.key,
        "user":{
            "email":user.email,
            "name":user.name
        }
    })

    

