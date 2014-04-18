from mobiledevice.models import MobileDevice
from django.contrib import admin


class MobileDevAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,           {'fields': ['product_type',
                                     'brand_name',
                                     'model_name',
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
    list_display = ('owner_name', 'owner_lastname',
                    'email', 'khas_id',
                    'delivery_date', 'current_situation',
                    'survelliance_key', 'received_or_not')
    list_filter = ['delivery_date', 'current_situation']
    search_fields = ['survelliance_key', 'owner_name', 'owner_lastname']

admin.site.register(MobileDevice, MobileDevAdmin)
