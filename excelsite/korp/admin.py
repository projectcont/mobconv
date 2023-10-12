from django.contrib import admin

from .models import *

class KursAdmin(admin.ModelAdmin):
    list_display = ('time_create', 'time_write', 'eur', 'usd',)
    search_fields = ('eur', 'usd', 'time_write', )
    list_editable = ('eur','usd',)
    list_filter = ('time_create', 'eur', 'usd',)
    #list_display_links = ('title',)


admin.site.register(Valuta, KursAdmin)
