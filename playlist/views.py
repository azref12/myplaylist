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

from .models import *
from .serializers import *
from category.models import category, genre
from kdrama.models import kdrama

@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def playlist_list (request):
    
        mymodels = playlist
        myserializer = PlaylistSerializer

        if request.method == 'GET':
            
                mymodels = playlist.objects.all()
                myserializer = PlaylistSerializer (mymodels, many=True)
                
                return JsonResponse({'message' : 'successfully', 'results' : myserializer.data})
    
        if request.method == 'POST':
            try :
                localrequest = JSONParser().parse(request)
                mastermodel = playlist.objects.all()
                masterserializer = myserializer (mastermodel, data=localrequest)
                
                if masterserializer.is_valid():
                        idcategory = category.objects.filter(id_category=localrequest['id_category']).first()
                        idgenre = genre.objects.filter(id_genre=localrequest['id_genre']).first()
                        idkdrama = kdrama.objects.filter(id_kdrama=localrequest['id_kdrama']).first()

                        playlist_save = playlist (
                                        id_category = idcategory,
                                        id_genre = idgenre,
                                        id_kdrama = idkdrama
                                    )
                        playlist_save.save()

                        mastermodel = playlist.objects.all()
                        masterserializer = myserializer (mastermodel, many=True)
                        
                        return JsonResponse ({'message' : 'successfully','results' : masterserializer.data})
                return JsonResponse(masterserializer.errors, status=400)       
            except playlist.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)