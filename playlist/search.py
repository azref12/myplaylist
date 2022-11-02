from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@csrf_exempt
@api_view(["POST","GET"])
@permission_classes([AllowAny])
def Search_List(request) :

    if request.method == 'GET':
    
        try :
            x = request.GET['title']
            ModelPlaylist = list(playlist.objects.all().extra(
            select ={"id_playlist":'playlist_playlist.id_playlist',"namavoucher":'voucher_voucher.nama_voucher', "status": "redem_playlist.status",
                "kode_voucher":"voucher_voucher.kode_voucher","expired":"voucher_voucher.expired","url":"voucher_voucher.url" }, 
            tables=['category_category','genre_genre','playlist_playlist'], where=['redem_playlist.idvoucher=voucher_voucher.id_voucher and userid='+x])
                .values('id_voucher','namavoucher', 'status', 'kode_voucher','expired','url'))
 
            formater = {
                "playlist": ModelPlaylist,
            }
                
            return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : formater})
        except playlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)