from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters
from url_filter.integrations.drf import DjangoFilterBackend

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework import status

from .models import playlist 
from .serializers import PlaylistSerializer
from django.db.models import Q

class PlayList_List (generics.ListCreateAPIView):
    # queryset = playlist.objects.all()
    # serializer_class = PlaylistSerializer 
    # DecodedGenerator = api_view
    # permission_classes = [AllowAny]

    def get(self, request):
        queryset = playlist.objects.all()
        serializer_class = PlaylistSerializer (queryset, many=True)

        formater = {
            "playlist": serializer_class.data
        }

        return Response({'status': True, 'message': 'Successfully', 'results': formater}, status=201)

    def post(self, request, *args, **kwargs):
        queryset = request.data.get('image_list', False)
        serializer_class = PlaylistSerializer (data=request.data, context={'request': request})
        if serializer_class.is_valid():
            serializer_class.save()

            formater = {
                "playlist": serializer_class.data
            }

            return Response({'Status': True, 'message': 'Image upload successfully',
                             'results': formater})
        else:
            return Response({'Status': False, 'message': 'Error!! make sure field  is not empty',
                             'results': formater})


class PlayList_Detail (generics.RetrieveUpdateDestroyAPIView):
    # queryset = playlist.objects.all()
    # serializer_class = PlaylistSerializer 
    # DecodedGenerator = api_view
    # permission_classes = [AllowAny]

    # Retrieve, update or destroy (get,put,delete) :

    def retrieve(self, request, *args, **kwargs):

        try:
            pk = self.kwargs.get('pk')
            object = playlist.objects.get(id_playlist=kwargs['pk'])
            serializer = PlaylistSerializer (object)

            return Response(serializer.data)
        except playlist.DoesNotExist:
            return Response({'message': 'id not found!!!', 'status' : False}, status=400)

    def put(self, request, pk):
        queryset = playlist.objects.get(id_playlist=pk)
        serializer_class = PlaylistSerializer (queryset, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = playlist.objects.get(id_playlist=pk)
        queryset.delete()
        return Response({"message": "id has been delete"})

@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def getbytitle (request, *args, **kwargs):

    if request.method == 'GET':
   
        try :
            x = request.GET['id_playlist']
            localmodel = list(playlist.objects.all().extra(
            select ={"id_playlist":'playlist_playlist.id_playlist',"title":'playlist_playlist.title',
                     "director": "playlist_playlist.director","writer":"playlist_playlist.writer",
                     "release_date":"playlist_playlist.release_date","runtime":"playlist_playlist.runtime",
                     "language":"playlist_playlist.language","country":"playlist_playlist.country"}, 
            tables=['playlist_playlist'], where=['id_playlist = '+ x]).values('id_playlist','title', 'director', 'writer','release_date','runtime','language','country'))

            formater = {
                "playlist": localmodel,
            }
            
            return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : formater})
        except playlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# @csrf_exempt
# @api_view(["GET"])
# @permission_classes([AllowAny])
# def search_by_title (request):

#     if request.method == 'GET':
        
#         try :
#             # title=request.GET['title']
#             localmodel = playlist.objects.filter(title=request.GET['title'])
#             localserializer = PlaylistSerializer (localmodel, many=True)

#             formater = {
#                 "playlist": localserializer.data
#             }

#             return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : formater})
#         except playlist.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
