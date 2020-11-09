from django.contrib import admin

from .models import BdpGeneralFiltrada, BdpDetalladaFiltrada, BdlDetalladaFiltrada, Coordenadas

admin.site.register(BdpGeneralFiltrada)
admin.site.register(BdpDetalladaFiltrada)
admin.site.register(BdlDetalladaFiltrada)
admin.site.register(Coordenadas)
