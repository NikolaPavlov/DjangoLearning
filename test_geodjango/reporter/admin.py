from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Incident


# Register your models here.
class IncidentAdmin(admin.ModelAdmin):
    # list_display=('name', 'location')
    pass


admin.site.register(Incident, LeafletGeoAdmin)
# admin.site.register(Incident, IncidentAdmin)
