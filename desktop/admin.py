from desktop.models import Desktop
from django.contrib import admin


class DesktopAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,           {'fields': ['product_type',
                                     'serial_number',
                                     'brand_name',
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
                    'current_situation', 'serial_number',
                    'received_or_not')
    list_filter = ['delivery_date', 'current_situation']
    search_fields = ['serial_number', 'survelliance_key',
                     'owner_name', 'owner_lastname', 'brand_name']

admin.site.register(Desktop, DesktopAdmin)
