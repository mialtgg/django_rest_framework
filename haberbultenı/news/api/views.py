from rest_framework  import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from news.models import Blog,Makale_2
from news.api.serializers import  MakaleSerializer

@api_view(['GET'])
def makale_list_create_api_view(request):
    if request.method=='GET':
        makaleler = Makale_2.objects.filter(aktif=True) #burada nenelerden oluşan bir queryset var
        serializer = MakaleSerializer(makaleler ,many = True) #queryset
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = MakaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)