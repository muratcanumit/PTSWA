from device.models import Device
from django.contrib import admin


class DeviceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,           {'fields': ['device_type',
                                     'serial_number',
                                     'brand_name',
                                     'model_name',
                                     'problem',
                                     'current_status',
                                     'owner_name',
                                     'owner_lastname',
                                     'phone_number',
                                     'email',
                                     'khas_id']}),
        ('Delivery Date', {'fields': ['delivery_date'],
                           'classes': ['collapse']}),
    ]
    list_display = ('survelliance_key', 'owner_name',
                    'owner_lastname', 'record_date',
                    'current_status', 'serial_number',
                    'received_or_not')
    list_filter = ['record_date', 'current_status', 'device_type']
    search_fields = ['serial_number', 'survelliance_key',
                     'owner_name', 'owner_lastname', 'brand_name',
                     'model_name']

admin.site.register(Device, DeviceAdmin)
