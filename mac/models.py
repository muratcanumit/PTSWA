from django.db import models
from hashlib import sha1
from random import random
from libs.mailsender import send_key_email

PROD_TYPE = (
    ('MacBook Air', 'MacBook Air'),
    ('MacBook Pro', 'MacBook Pro'),
    ('Mac mini', 'Mac mini'),
    ('iMac', 'iMac'),
    ('Mac Pro', 'Mac Pro'),
    ('OS X Mavericks', 'OS X Mavericks'),
)

PROD_BRAND_MAC = (
    ('Apple', 'Apple'),
)

PROD_SITUATION = (
    ('Teknik Serviste', 'Teknik Serviste'),
    ('Teslime Hazir', 'Teslime Hazir'),
    ('Teslim Edildi', 'Teslim Edildi'),
)


class Mac (models.Model):
    product_type = models.CharField(max_length=25,
                                    choices=PROD_TYPE,
                                    verbose_name="Urunun Tipi")
    serial_number = models.CharField(max_length=50,
                                     verbose_name="Seri Numarasi")
    brand_name = models.CharField(max_length=25,
                                  choices=PROD_BRAND_MAC,
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

    def save(self, *args, **kwargs):
        if not self.id:
            message = ("Servise biraktiginiz urununuzun takip anahtari: " +
                       self.survelliance_key + " , ile Sitemizden Durumunu "
                       "takip edebilirsiniz. \nIyi Gunler.")
            send_key_email(self.email, message)
        else:
            message = ("Urununuzun islemi bitmis olup, teslime hazirdir." +
                       "\nServise biraktiginiz urununuzun takip anahtari: "
                       + self.survelliance_key + " , ile Sitemizden Durumunu "
                       "takip edebilirsiniz. \nIyi Gunler.")
            send_key_email(self.email, message)

        super(Mac, self).save(*args, **kwargs)


class Meta:
        ordering = ['-delivery_date']
