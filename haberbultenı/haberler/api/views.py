from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view  

from haberler.models import Makale
from haberler.api.serializers import MakaleSerializers

@api_view(['GET','POST'])
def makale_list_create_api_view(request):

    if request.method == 'GET' :
        makaleler = Makale.objects.filter(aktif = True)
        serializer = MakaleSerializers (makaleler ,many =True) 
        return  Response(serializer.data)
    elif request.method == 'POST':
        serializer = MakaleSerializers(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def makale_detail_api_view(request,pk):
    try:
        makale_instance = Makale.objects.get(pk=pk)
    except Makale.DoesNotExist:
        return Response(
        {
            'errors':
            {
                'code' : 404,
                'message' :f'Böyle bir id{{pk}} ile ilgili makale bulunamadı'
            }
        },
        status=status.HTTP_404_NOT_FOUND
    )
    if  request.method =='GET':
        serializer=MakaleSerializers(makale_instance)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = MakaleSerializers(makale_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method ==  'DELETE' :
        makale_instance.delete()
        return Response(
            {
                'işlem':{
                    'code': 204,
                    'message' :f'{{pk}} id numaralı makale silindi'
                }
            },
            status=status.HTTP_204_NO_CONTENT
        )
