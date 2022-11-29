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

from .models import kdrama
from .serializers import KdramaSerializer

class Kdrama_List (generics.ListCreateAPIView):
    # queryset = kdrama.objects.all()
    # serializer_class = KdramaSerializer 
    # DecodedGenerator = api_view
    # permission_classes = [AllowAny]

    def get(self, request):
        queryset = kdrama.objects.all()
        serializer_class = KdramaSerializer (queryset, many=True)

        formater = {
            "kdrama": serializer_class.data
        }

        return Response({'status': True, 'message': 'Successfully', 'results': formater}, status=201)

    def post(self, request, *args, **kwargs):
        queryset = request.data.get('image_list', False)
        serializer_class = KdramaSerializer (data=request.data, context={'request': request})
        if serializer_class.is_valid():
            serializer_class.save()

            formater = {
                "kdrama": serializer_class.data
            }

            return Response({'Status': True, 'message': 'Image upload successfully',
                             'results': formater})
        else:
            return Response({'Status': False, 'message': 'Error!! make sure field  is not empty',
                             'results': formater})


class Kdrama_Detail (generics.RetrieveUpdateDestroyAPIView):
    # queryset = kdrama.objects.all()
    # serializer_class = KdramaSerializer 
    # DecodedGenerator = api_view
    # permission_classes = [AllowAny]

    # Retrieve, update or destroy (get,put,delete) :

    def retrieve(self, request, *args, **kwargs):

        try:
            pk = self.kwargs.get('pk')
            object = kdrama.objects.get(id_kdrama=kwargs['pk'])
            serializer = KdramaSerializer (object)

            return Response(serializer.data)
        except kdrama.DoesNotExist:
            return Response({'message': 'id not found!!!', 'status' : False}, status=400)

    def put(self, request, pk):
        queryset = kdrama.objects.get(id_kdrama=pk)
        serializer_class = KdramaSerializer (queryset, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = kdrama.objects.get(id_kdrama=pk)
        queryset.delete()
        return Response({"message": "id has been delete"})