from rest_framework import serializers
from news.models import Makale_2
class MakaleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only =True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    aktif = serializers.BooleanField()
    
    güncellenme_tarihi = serializers.DateField(read_only =True)
    yayimlanma_tarihi =serializers.DateField()
    yaratilma_tarihi = serializers.DateField(read_only=True)

def create(self,validated_data):
    return Makale_2.objects.create(**validated_data)

def update(self,instance, validated_data):
    instance.yazar = validated_data.get('yazar',instance.yazar)
    instance.baslik = validated_data.get('başlik', instance.baslik)
    instance.aciklama = validated_data.get('açiklama',instance.acıklama)
    instance.metin = validated_data.get('metin' ,instance.metin)
    instance.sehir = validated_data.get('şehir' ,instance.sehir)
    instance.yayimlanma_tarihi=validated_data.get('yayınlanma tarihi',instance.yayimlanma_tarihi)
    instance.aktif = validated_data.get('aktif', instance.aktif)
    
    instance.save()
    return instance



  
    

