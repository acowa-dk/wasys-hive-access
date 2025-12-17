from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
from .models import Unit

class UnitAdmin(ModelAdmin):
    fields = [
        "name",
        "scada_name",
        "imei",
        "ip_address",
        "address",
        "gps_latitude",
        "gps_longitude",
        "input_type_id",
    ]

    list_display  = ["name", "scada_name", "imei", "ip_address", "unit_type"]


admin.site.register(Unit, UnitAdmin)
