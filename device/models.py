from django.db import models
import uuid
from libs.mailsender import send_key_email
from django.utils.translation import ugettext as _
from libs.choices import DEVICE_TYPES, DEVICE_STATUS, DEVICE_BRANDS


class Device (models.Model):
    survelliance_key = models.CharField(max_length=25,
                                        unique=True,
                                        verbose_name=_('Record Key of Device'))

    device_type = models.CharField(max_length=25,
                                   choices=DEVICE_TYPES,
                                   verbose_name=_('Type of Device'))

    serial_number = models.CharField(max_length=50,
                                     blank=True, null=True,
                                     verbose_name=_('Serial Number'))

    brand_name = models.CharField(max_length=25,
                                  choices=DEVICE_BRANDS,
                                  blank=True, null=True,
                                  verbose_name=_('Name of Brand'))

    model_name = models.CharField(max_length=25,
                                  blank=True, null=True,
                                  verbose_name=_('Name of Model'))

    problem = models.TextField(max_length=250,
                               verbose_name=_('Problem of Device'))

    current_status = models.CharField(max_length=25,
                                      choices=DEVICE_STATUS,
                                      verbose_name=_('Device Status'))

    record_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name=_('Record Date'))

    delivery_date = models.DateTimeField(blank=True, null=True,
                                         verbose_name=_('Delivery Date'))

    owner_name = models.CharField(max_length=25,
                                  verbose_name=_('Name of Device Owner'))

    owner_lastname = models.CharField(max_length=25,
                                      verbose_name=_('Lastname'))

    phone_number = models.CharField(max_length=11,
                                    blank=True, null=True,
                                    verbose_name=_('Phone Number'))

    email = models.EmailField(verbose_name=_('Email Address'))

    khas_id = models.CharField(max_length=20,
                               blank=True, null=True,
                               verbose_name="KHAS ID")

    def received_or_not(self):
        if self.current_status == _('Delivered'):
            return True
        return False
    received_or_not.boolean = True
    received_or_not.short_description = _('Delivered?')

    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                survelliance_key = str(uuid.uuid1())[:25]
                if len(Device.objects.filter(survelliance_key=survelliance_key)) == 0:
                    self.survelliance_key = survelliance_key
                    break

            message = (_('Survelliance key of your device ') +
                       _('that you left at help desk is : ') +
                       self.survelliance_key +
                       '\n\n' +
                       _('From the address that www.khashelpdesk.com ,') +
                       _('you can search your device status using the key. ') +
                       _('Have a nice day.') +
                       '\n\n' + _('Kadir Has University Help Desk'))

            send_key_email(self.email, message)

        else:
            message = (_('Progress of your device is completed.') +
                       '\n\n' +
                       _('Survelliance key of your device is : ') +
                       self.survelliance_key +
                       '\n\n' +
                       _('From the address that www.khashelpdesk.com ,') +
                       _('you can search your device status using the key. ') +
                       _('Have a nice day.') +
                       '\n\n' + _('Kadir Has University Help Desk'))

            send_key_email(self.email, message)

        super(Device, self).save(*args, **kwargs)


class Meta:
        ordering = ['-record_date']
# _('or directly reach with clicking the link.') +
#                       '\n\n' + 'www.khashelpdesk.com/device/search/' +
#                       self.survelliance_key + '/status/\n\n' +
