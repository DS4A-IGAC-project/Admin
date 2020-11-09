from django.contrib import admin

from .models import BdpGeneralFiltrada, BdpDetalladaFiltrada, BdlDetalladaFiltrada, Coordenadas


class NoIndexAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("index",)
        return super(NoIndexAdmin, self).get_form(request, obj, **kwargs)


class BDPGeneralAdmin(NoIndexAdmin):
    list_display = ("cod_perfil", "fecha_ajustada")
    list_filter = ("fecha_ajustada", )
    search_fields = ("cod_perfil", )


class BDPDetalladaAdmin(NoIndexAdmin):
    list_display = ("horizontes", "cod_perfil")
    list_filter = ("cod_perfil", )
    search_fields = ("horizontes", )


class BDLDetalladaAdmin(NoIndexAdmin):
    list_display = ("horizontes", "cod_perfil")
    list_filter = ("cod_perfil", )
    search_fields = ("horizontes__horizontes", )


class CoordenadasAdmin(NoIndexAdmin):
    list_display = ("cod_perfil", "latitud", "longitud")
    search_fields = ("cod_perfil__cod_perfil", )


admin.site.register(BdpGeneralFiltrada, BDPGeneralAdmin)
admin.site.register(BdpDetalladaFiltrada, BDPDetalladaAdmin)
admin.site.register(BdlDetalladaFiltrada, BDLDetalladaAdmin)
admin.site.register(Coordenadas, CoordenadasAdmin)
