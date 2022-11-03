from django.shortcuts import render
import datetime 
from codecs import ignore_errors
from functools import partial
from inspect import isfunction
from re import X

from django.db import DatabaseError, transaction
from django.db.models.aggregates import Max
from django.db.utils import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import translation
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import category, genre
from .serializers import CategorySerilaizer, GenreSerilaizer

@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def category_list (request):
    
        mymodels = category
        myserializer = CategorySerilaizer

        if request.method == 'GET':
            
                mymodels = category.objects.all()
                myserializer = CategorySerilaizer (mymodels, many=True)
                
                return JsonResponse({'message' : 'successfully', 'results' : myserializer.data})
    
        if request.method == 'POST':
            try :
                localrequest = JSONParser().parse(request)
                mastermodel = category.objects.all()
                masterserializer = myserializer (mastermodel, data=localrequest)
                
                if masterserializer.is_valid():
                        
                        category_save = category (
                                        category_name = localrequest['category_name']
                                    )
                        category_save.save()

                        mastermodel = category.objects.all()
                        masterserializer = myserializer (mastermodel, many=True)
                        
                        return JsonResponse ({'message' : 'successfully','results' : masterserializer.data})
                return JsonResponse(masterserializer.errors, status=400)       
            except category.DoesNotExist:
                return JsonResponse({'message' : 'unsuccessfully !!'}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny]) 
def category_detail (request, pk):
    
        mymodels = category
        myserializer = CategorySerilaizer
        
        try:
                localmodel = mymodels.objects.get(id_category=pk)
        except mymodels.DoesNotExist:
                return JsonResponse({'message' : 'id not found!!', 'status' : False},status=404)

        if request.method == 'GET':
        
                localserializer = myserializer(localmodel)
                return JsonResponse(localserializer.data)
    
        if request.method == 'PUT':
                try:
                        localrequest = JSONParser().parse(request)

                        checkcategory = category.objects.filter(id_category=pk).count()
                        if checkcategory != 0:
                                modelcategory = category.objects.get(id_category=pk)
                                categoryserializer = CategorySerilaizer(modelcategory, data=localrequest, partial=True)

                                if categoryserializer.is_valid():
                                        categoryserializer.save(
                                                category_name=localrequest['category_name']
                                        )

                                        return JsonResponse({"message": "successfully", "results": 'category_name has been change'}, status=200)
                        else:
                                return JsonResponse({"message": "unsuccessfully", "results": "id_category do not exist"}, status=400)

                except category.DoesNotExist:
                        return JsonResponse({"message": "unsuccessfully", "results": "error"})

        elif request.method == 'DELETE': 
                localmodel.delete() 
                localmodel = mymodels.objects.all()
                localserializer = myserializer(localmodel, many=True)

        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                status=201)    

@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def genre_list (request):
    
        mymodels = genre
        myserializer = GenreSerilaizer

        if request.method == 'GET':
            
                mymodels = genre.objects.all()
                myserializer = GenreSerilaizer (mymodels, many=True)
                
                return JsonResponse({'message' : 'successfully', 'results' : myserializer.data})
    
        if request.method == 'POST':
            try :
                localrequest = JSONParser().parse(request)
                mastermodel = genre.objects.all()
                masterserializer = myserializer (mastermodel, data=localrequest)
                
                if masterserializer.is_valid():
                        
                        genre_save = genre (
                                        genre = localrequest['genre']
                                    )
                        genre_save.save()

                        mastermodel = genre.objects.all()
                        masterserializer = myserializer (mastermodel, many=True)
                        
                        return JsonResponse ({'message' : 'successfully','results' : masterserializer.data})
                return JsonResponse(masterserializer.errors, status=400)       
            except genre.DoesNotExist:
                return JsonResponse({'message' : 'unsuccessfully !!'}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny]) 
def genre_detail (request, pk):
    
        mymodels = genre
        myserializer = GenreSerilaizer
        
        try:
                localmodel = mymodels.objects.get(id_genre=pk)
        except mymodels.DoesNotExist:
                return JsonResponse({'message' : 'id not found!!', 'status' : False},status=404)

        if request.method == 'GET':
        
                localserializer = myserializer(localmodel)
                return JsonResponse(localserializer.data)
    
        if request.method == 'PUT':
                try:
                        localrequest = JSONParser().parse(request)

                        checkgenre = genre.objects.filter(id_genre=pk).count()
                        if checkgenre != 0:
                                modelgenre = genre.objects.get(id_genre=pk)
                                genreserializer = GenreSerilaizer (modelgenre, data=localrequest, partial=True)

                                if genreserializer.is_valid():
                                        genreserializer.save(
                                                genre=localrequest['genre']
                                        )

                                        return JsonResponse({"message": "successfully", "results": 'genre has been change'}, status=200)
                        else:
                                return JsonResponse({"message": "unsuccessfully", "results": "id_genre do not exist"}, status=400)

                except genre.DoesNotExist:
                        return JsonResponse({"message": "unsuccessfully", "results": "error"})

        elif request.method == 'DELETE': 
                localmodel.delete() 
                localmodel = mymodels.objects.all()
                localserializer = myserializer(localmodel, many=True)

        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                status=201) 
