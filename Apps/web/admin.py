from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# -------------------------------------
class ResourceProduct(resources.ModelResource):
    class Meta:
        model = product

class AdminProduct(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['pk_producto', 'codigo', 'nombre', 'descripcion', 'precio']
    resource_class = ResourceProduct

admin.site.register(product, AdminProduct)
