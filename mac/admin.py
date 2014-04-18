from mac.models import Mac
from django.contrib import admin


class MacAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,           {'fields': ['product_type',
                                     'serial_number',
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
    list_display = ('serial_number', 'owner_name',
                    'owner_lastname', 'email', 'khas_id',
                    'delivery_date', 'current_situation',
                    'survelliance_key', 'received_or_not')
    list_filter = ['delivery_date', 'current_situation']
    search_fields = ['serial_number', 'survelliance_key',
                     'owner_name', 'owner_lastname']

admin.site.register(Mac, MacAdmin)
