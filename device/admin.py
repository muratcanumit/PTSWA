from device.models import Device, SearchHistory
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
    list_display = ('survelliance_key', 'device_type',
                    'brand_name', 'model_name',
                    'owner_name', 'owner_lastname',
                    'record_date', 'current_status',
                    'serial_number')
    list_filter = ['record_date', 'current_status', 'device_type']
    search_fields = ['serial_number', 'survelliance_key',
                     'owner_name', 'owner_lastname', 'brand_name',
                     'model_name']

admin.site.register(Device, DeviceAdmin)


class SearchHistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,           {'fields': ['survelliance_key']}),
    ]

admin.site.register(SearchHistory, SearchHistoryAdmin)
