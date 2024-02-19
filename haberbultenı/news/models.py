
from django.db import models

class Makale (models.Model):
    yazar = models.CharField(max_length=150)
    baslık = models.CharField(max_length=120)
    acıklama = models.CharField(max_length=200)
    metin = models.TextField()
    sehir = models.CharField(max_length=120)
    yayımlanma_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.baslık
