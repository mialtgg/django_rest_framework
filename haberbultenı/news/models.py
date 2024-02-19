
from django.db import models

class Blog (models.Model):
    yazar = models.CharField(max_length=150)
    baslik = models.CharField(max_length=120)
    aciklama = models.CharField(max_length=200)
    metin = models.TextField()
    sehir = models.CharField(max_length=120)
    yayimlanma_tarihi = models.DateTimeField()
    güncellenme_tarihi = models.DateTimeField(auto_now =True)
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.baslik
    
    
class Makale_2 (models.Model):
    yazar = models.CharField(max_length=150)
    baslik = models.CharField(max_length=120)
    aciklama = models.CharField(max_length=200)
    metin = models.TextField()
    sehir = models.CharField(max_length=120)
    yayimlanma_tarihi = models.DateTimeField()
    güncellenme_tarihi = models.DateTimeField(auto_now =True)
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.baslik
