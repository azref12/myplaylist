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

from . models import recommendation
from . serializers import RecommendSerializer
from playlist.models import playlist
from playlist.serializers import PlaylistSerializer

@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def recommend_list (request):
    
        mymodels = recommendation
        myserializer = RecommendSerializer

        if request.method == 'GET':
            
                mymodels = recommendation.objects.all()
                myserializer = RecommendSerializer (mymodels, many=True)
                
                return JsonResponse({'message' : 'successfully', 'results' : myserializer.data})
    
        if request.method == 'POST':
            try :
                localrequest = JSONParser().parse(request)
                mastermodel = recommendation.objects.all()
                masterserializer = myserializer (mastermodel, data=localrequest)
                
                if masterserializer.is_valid():
                        idplaylist = playlist.objects.filter(id_playlist=localrequest['id_playlist']).first()
                        
                        recommend_save = recommendation (
                                        id_playlist = idplaylist
                                    )
                        recommend_save.save()

                        mastermodel = recommendation.objects.all()
                        masterserializer = myserializer (mastermodel, many=True)
                        
                        return JsonResponse ({'message' : 'successfully','results' : masterserializer.data})
                return JsonResponse(masterserializer.errors, status=400)       
            except recommendation.DoesNotExist:
                return JsonResponse({'message' : 'unsuccessfully !!'}, status=status.HTTP_404_NOT_FOUND)
            
@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def playlist_id(request, pk):

    if request.method == 'GET':

        countmodel = playlist.objects.filter(id_playlist=pk).count()
        if countmodel != 0:
            localmodel = playlist.objects.filter(id_playlist=pk)
            localserializer = PlaylistSerializer (localmodel, many=True)

            formater = {
                "playlist": localserializer.data
            }

            return JsonResponse({"message": "successfully", "results": formater})
        else:
            return JsonResponse({"message": "unsuccessfully", "results": "playlist not found!!!"})

# @csrf_exempt
# @api_view(["PUT", "GET"])
# @permission_classes([AllowAny])
# def getbytitle (request, *args, **kwargs):

#     if request.method == 'GET' :
#         try :
#             Mymodels = playlist.objects.filter(title=request.GET['title'])
#             Serializers = PlaylistSerializer (Mymodels, many=True)

#             formater = {
#                 # "master" : myserializers.data,
#                 "details" : Serializers.data
#             }

#             return JsonResponse({'message': 'successfully', 'status': True, 'count': 1, 'results': formater})
#         except playlist.DoesNotExist:
#             return JsonResponse({'message': 'unsuccessfully', 'status': False, 'count': 1, 'results': "title not found!!"})
