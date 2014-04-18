from django.db import models
from hashlib import sha1
from random import random

PROD_TYPE = (
    ('Android Telefon', 'Android Telefon'),
    ('WindowsPhone', 'WindowsPhone'),
    ('iPhone', 'iPhone'),
    ('Android Tablet', 'Android Tablet'),
    ('iPad', 'iPad'),
    ('Windows Tablet', 'Windows Tablet'),
)

PROD_BRAND_MOBILE = (
    ('Apple', 'Apple'),
    ('Samsung', 'Samsung'),
    ('HTC', 'HTC'),
    ('LG', 'LG'),
    ('Sony', 'Sony'),
    ('Nokia', 'Nokia'),
    ('Blackberry', 'Balckberry'),
)

PROD_SITUATION = (
    ('Teknik Serviste', 'Teknik Serviste'),
    ('Teslime Hazir', 'Teslime Hazir'),
    ('Teslim Edildi', 'Teslim Edildi'),
)


class MobileDevice (models.Model):
    product_type = models.CharField(max_length=25,
                                    choices=PROD_TYPE,
                                    verbose_name="Urunun Tipi")
    brand_name = models.CharField(max_length=50,
                                  choices=PROD_BRAND_MOBILE,
                                  verbose_name="Urunun Markasi")
    model_name = models.CharField(max_length=25,
                                  verbose_name="Urunun Modeli")
    problem = models.TextField(max_length=250,
                               verbose_name="Urunun Sorunu")
    current_situation = models.CharField(max_length=25,
                                         choices=PROD_SITUATION,
                                         verbose_name="Urunun Durumu")
    delivery_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Help Desk Kayit Tarihi")
    receive_date = models.DateTimeField(verbose_name="Teslim Tarihi",
                                        blank=True, null=True)
    survelliance_key = models.CharField(max_length=30,
                                        default=sha1(str(random())).hexdigest(),
                                        unique=True,
                                        verbose_name="Takip Anahtari")
    owner_name = models.CharField(max_length=25,
                                  verbose_name="Urun Sahibinin Adi")
    owner_lastname = models.CharField(max_length=25,
                                      verbose_name="Urun Sahibinin Soyadi")
    phone = models.CharField(max_length=10,
                             verbose_name="Telefon Numarasi")
    email = models.EmailField(verbose_name="E-Posta Adresi")
    khas_id = models.CharField(max_length=20, verbose_name="KHAS ID",
                               blank=True, null=True)

    def received_or_not(self):
        return self.current_situation == "Teslim Edildi"
    received_or_not.boolean = True
    received_or_not.short_description = 'Teslim Edildi mi?'


class Meta:
        ordering = ['-delivery_date']
