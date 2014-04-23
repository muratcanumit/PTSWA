from django.db import models
import uuid
from libs.mailsender import send_key_email
from libs.choices import DEVICE_TYPES, DEVICE_STATUS, DEVICE_BRANDS


class Device (models.Model):
    survelliance_key = models.CharField(max_length=25,
                                        unique=True,
                                        verbose_name="Record Key of Device")

    device_type = models.CharField(max_length=25,
                                   choices=DEVICE_TYPES,
                                   verbose_name="Type of Device")

    serial_number = models.CharField(max_length=50,
                                     verbose_name="Serial Number",
                                     blank=True, null=True)

    brand_name = models.CharField(max_length=25,
                                  choices=DEVICE_BRANDS,
                                  blank=True, null=True,
                                  verbose_name="Name of Brand")

    model_name = models.CharField(max_length=25,
                                  verbose_name="Name of Model",
                                  blank=True, null=True)

    problem = models.TextField(max_length=250,
                               verbose_name="Problem of Device")

    current_status = models.CharField(max_length=25,
                                      choices=DEVICE_STATUS,
                                      verbose_name="Device Status")

    record_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name="Record Date")

    delivery_date = models.DateTimeField(verbose_name="Delivery Date",
                                         blank=True, null=True)

    owner_name = models.CharField(max_length=25,
                                  verbose_name="Name of Device Owner")

    owner_lastname = models.CharField(max_length=25,
                                      verbose_name="Lastname")

    phone_number = models.CharField(max_length=11,
                                    verbose_name="Phone Number",
                                    blank=True, null=True)

    email = models.EmailField(verbose_name="Email Address")

    khas_id = models.CharField(max_length=20, verbose_name="KHAS ID",
                               blank=True, null=True)

    def received_or_not(self):
        return self.current_situation == "Delivered"
    received_or_not.boolean = True
    received_or_not.short_description = 'Delivered?'

    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                survelliance_key = str(uuid.uuid1())[:25]
                if len(Device.objects.filter(survelliance_key=survelliance_key)) == 0:
                    self.survelliance_key = survelliance_key
                    break

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

        super(Device, self).save(*args, **kwargs)


class Meta:
        ordering = ['-delivery_date']
