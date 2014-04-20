from otherdevice.models import OtherDevice
from django.contrib import admin


class OtherDevAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,           {'fields': ['product_type',
                                     'brand_name',
                                     'model_name',
                                     'serial_number',
                                     'problem',
                                     'current_situation',
                                     'owner_name',
                                     'owner_lastname',
                                     'phone',
                                     'email',
                                     'khas_id']}),
        ('Teslim Tarihi', {'fields': ['receive_date'],
                           'classes': ['collapse']}),
    ]
    list_display = ('survelliance_key', 'owner_name',
                    'owner_lastname', 'delivery_date',
                    'model_name', 'current_situation',
                    'serial_number', 'received_or_not')
    list_filter = ['delivery_date', 'current_situation']
    search_fields = ['serial_number', 'survelliance_key',
                     'owner_name', 'owner_lastname']

admin.site.register(OtherDevice, OtherDevAdmin)
