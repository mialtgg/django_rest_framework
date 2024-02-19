from rest_framework import serializers
from news.models import Makale





class MakaleSerializer(serializers.Serializer):
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayınlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratılma_tarihi = serializers.DateField(read_only=True)
    güncellenme_tarihi = serializers.DateField(read_only =True)

def create(self,validated_data):
    return Makale.objects.create(**validated_data)

def update(self,instance, validated_data):
    instance.yazar = validated_data.get('yazar',instance.yazar)
    instance.baslik = validated_data.get('başlık', instance.baslik)
    instance.aciklama = validated_data.get('açıklama',instance.aciklama)
    instance.metin = validated_data.get('metin' ,instance.metin)
    instance.sehir = validated_data.get('şehir' ,instance.sehir)
    instance.yayınlanma_tarihi=validated_data.get('yayınlanma tarihi',instance.yayınlanma_tarihi)
    instance.aktif = validated_data.get('aktif', instance.aktif)
    
    instance.save()
    return instance



  
    

