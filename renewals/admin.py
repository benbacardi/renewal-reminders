'''Renewals admin classes'''
from django.contrib import admin

from .models import Vehicle, Renewable


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plate', 'nickname', 'type', 'colour', 'make', 'model', 'user')
    search_fields = ('plate', 'nickname', 'colour', 'make', 'model', 'user__username')
    list_filter = ('type',)


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Renewable, admin.ModelAdmin)
