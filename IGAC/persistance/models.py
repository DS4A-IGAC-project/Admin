from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class BdpGeneralFiltrada(models.Model):
    index = models.BigIntegerField(blank=True, null=True, db_column='index')
    cod_perfil = models.TextField(db_column='COD_PERFIL', primary_key=True, unique=True)
    simbolo_ucs = models.TextField(db_column='SIMBOLO_UCS', blank=True, null=True)
    tipo_ucs = models.TextField(db_column='TIPO_UCS', blank=True, null=True)
    departamento = models.TextField(db_column='DEPARTAMENTO', blank=True, null=True)
    clase_pendiente = models.TextField(db_column='CLASE_PENDIENTE', blank=True, null=True)
    porc_pendiente = models.TextField(db_column='PORC_PENDIENTE', blank=True, null=True)
    memoria = models.TextField(db_column='MEMORIA', blank=True, null=True)
    drenaje_interno = models.TextField(db_column='DRENAJE_INTERNO', blank=True, null=True)
    drenaje_externo = models.TextField(db_column='DRENAJE_EXTERNO', blank=True, null=True)
    drenaje_natural = models.TextField(db_column='DRENAJE_NATURAL', blank=True, null=True)
    profundidad_efectiva = models.TextField(db_column='PROFUNDIDAD_EFECTIVA', blank=True,
                                            null=True)
    longitud_pendiente = models.TextField(db_column='LONGITUD_PENDIENTE', blank=True,
                                          null=True)
    forma_pendiente = models.TextField(db_column='FORMA_PENDIENTE', blank=True, null=True)
    regimen_humedad = models.TextField(db_column='REGIMEN_HUMEDAD', blank=True, null=True)
    clase_erosion = models.TextField(db_column='CLASE_EROSION', blank=True, null=True)
    tipo_erosion = models.TextField(db_column='TIPO_EROSION', blank=True, null=True)
    grado_erosion = models.TextField(db_column='GRADO_EROSION', blank=True, null=True)
    tipo_pedregosidad = models.TextField(db_column='TIPO_PEDREGOSIDAD', blank=True,
                                         null=True)
    porc_pedregosidad_superficial_cubierta = models.TextField(db_column='PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA',
                                                              blank=True, null=True)
    clase_pedregosidad = models.TextField(db_column='CLASE_PEDREGOSIDAD', blank=True,
                                          null=True)
    fase_inundacion_encharcamiento = models.TextField(db_column='FASE_INUNDACION_ENCHARCAMIENTO', blank=True,
                                                      null=True)
    frecuencia_inundacion = models.TextField(db_column='FRECUENCIA_INUNDACION', blank=True,
                                             null=True)
    duracion_inundacion = models.TextField(db_column='DURACION_INUNDACION', blank=True,
                                           null=True)
    frecuencia_encharcamiento = models.TextField(db_column='FRECUENCIA_ENCHARCAMIENTO', blank=True,
                                                 null=True)
    duracion_encharcamiento = models.TextField(db_column='DURACION_ENCHARCAMIENTO', blank=True,
                                               null=True)
    caracteristicas_diagnosticas = models.TextField(db_column='CARACTERISTICAS_DIAGNOSTICAS', blank=True,
                                                    null=True)
    clasificacion_taxonomica = models.TextField(db_column='CLASIFICACION_TAXONOMICA', blank=True,
                                                null=True)
    familia_textural = models.TextField(db_column='FAMILIA_TEXTURAL', blank=True,
                                        null=True)
    epipedon = models.TextField(db_column='EPIPEDON', blank=True, null=True)
    endopedon_1 = models.TextField(db_column='ENDOPEDON_1', blank=True, null=True)
    endopedon_2 = models.TextField(db_column='ENDOPEDON_2', blank=True, null=True)
    fase_desp_fam_text = models.TextField(db_column='FASE_desp_fam_text', blank=True,
                                          null=True)
    fecha_ajustada = models.DateTimeField(db_column='Fecha_Ajustada')

    class Meta:
        # managed = False
        db_table = 'bdp_general_filtrada'
        verbose_name = 'BDP General'
        verbose_name_plural = '1. BDP General'

    def __str__(self):
        return f"{self.cod_perfil}"

    def __unicode__(self):
        return f"{self.cod_perfil}"


class BdpDetalladaFiltrada(models.Model):
    index = models.BigIntegerField(blank=True, null=True, db_column='index')
    horizontes = models.TextField(db_column='HORIZONTES', primary_key=True, unique=True)
    cod_perfil = models.ForeignKey(BdpGeneralFiltrada, on_delete=models.CASCADE, db_column='COD_PERFIL')
    profundidad_efectiva = models.TextField(db_column='PROFUNDIDAD_EFECTIVA', blank=True,
                                            null=True)
    color_matriz_seco1 = models.TextField(db_column='COLOR_MATRIZ_SECO1', blank=True,
                                          null=True)
    color_matriz_seco2 = models.TextField(db_column='COLOR_MATRIZ_SECO2', blank=True,
                                          null=True)
    color_matriz_humedo1 = models.TextField(db_column='COLOR_MATRIZ_HUMEDO1', blank=True,
                                            null=True)
    color_matriz_humedo2 = models.TextField(db_column='COLOR_MATRIZ_HUMEDO2', blank=True,
                                            null=True)
    consistencia_seco = models.TextField(db_column='CONSISTENCIA_SECO', blank=True,
                                         null=True)
    consistencia_humedo = models.TextField(db_column='CONSISTENCIA_HÚMEDO', blank=True,
                                           null=True)
    consist_mojado_pegj = models.TextField(db_column='CONSIST_MOJADO_PEGJ', blank=True,
                                           null=True)
    consist_mojado_pl = models.TextField(db_column='CONSIST_MOJADO_PL', blank=True,
                                         null=True)
    clase_erosion = models.TextField(db_column='CLASE_EROSION', blank=True, null=True)
    tipo_erosion = models.TextField(db_column='TIPO_EROSION', blank=True, null=True)
    grado_erosion = models.TextField(db_column='GRADO_EROSION', blank=True, null=True)
    evidencias_erosion = models.TextField(db_column='EVIDENCIAS_EROSION', blank=True,
                                          null=True)
    municipio = models.TextField(db_column='MUNICIPIO', blank=True, null=True)
    regimen_temperatura = models.TextField(db_column='REGIMEN_TEMPERATURA', blank=True,
                                           null=True)
    regimen_humedad = models.TextField(db_column='REGIMEN_HUMEDAD', blank=True, null=True)
    descripcion_horizonte = models.TextField(db_column='DESCRIPCIÓN_HORIZONTE', blank=True,
                                             null=True)
    horizonte_class = models.TextField(db_column='Horizonte_class', blank=True, null=True)
    izquierda_clas_tax = models.TextField(db_column='IZQUIERDA_CLAS_TAX', blank=True,
                                          null=True)
    derecha_clasificacion_tax = models.TextField(db_column='DERECHA_CLASIFICACION_TAX', blank=True,
                                                 null=True)
    metodo_ph = models.TextField(db_column='METODO_ph', blank=True, null=True)
    edafologo = models.TextField(db_column='EDAFOLOGO', blank=True, null=True)
    resultado_ph = models.FloatField(db_column='RESULTADO_ph', blank=True, null=True)
    espesor = models.FloatField(db_column='ESPESOR', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'bdp_detallada_filtrada'
        verbose_name = 'BDP Detallada'
        verbose_name_plural = '2. BDP Detallada'

    def __str__(self):
        return f"{self.horizontes}"

    def __unicode__(self):
        return f"{self.horizontes}"


class BdlDetalladaFiltrada(models.Model):
    index = models.AutoField(primary_key=True, db_column='index')
    cod_perfil = models.ForeignKey(BdpGeneralFiltrada, on_delete=models.CASCADE, db_column='COD_PERFIL')

    horizontes = ChainedForeignKey(
        BdpDetalladaFiltrada,
        chained_field='cod_perfil',
        chained_model_field='cod_perfil',
        show_all=False,
        auto_choose=True,
        sort=True,
        db_column='HORIZONTES'
    )

    # horizontes = models.ForeignKey(BdpDetalladaFiltrada, on_delete=models.CASCADE, db_column='HORIZONTES')
    clase_textural = models.TextField(db_column='Clase Textural', blank=True,
                                      null=True)
    carbono_organico_co_percentage_field = models.FloatField(db_column='CARBONO ORGANICO {CO Percentage}', blank=True,
                                                             null=True)
    ph_1_1_field = models.FloatField(db_column='pH {1:1}', blank=True,
                                     null=True)
    profundidades = models.FloatField(db_column='Profundidades', blank=True, null=True)
    cica = models.FloatField(db_column='CICA', blank=True, null=True)
    cice = models.FloatField(db_column='CICE', blank=True, null=True)
    cicv = models.FloatField(db_column='CICV', blank=True, null=True)
    number_0_kpa_field = models.FloatField(db_column='0{kPa}', blank=True,
                                           null=True)
    field_33_kpa_field = models.FloatField(db_column='-33{kPa}', blank=True,
                                           null=True)
    field_100_kpa_field = models.FloatField(db_column='-100{kPa}', blank=True,
                                            null=True)
    field_500_kpa_field = models.FloatField(db_column='-500{kPa}', blank=True,
                                            null=True)
    field_1500_kpa_field = models.FloatField(db_column='-1500{kPa}', blank=True,
                                             null=True)
    real_g_cm3_field = models.FloatField(db_column='REAL {g/cm3}', blank=True,
                                         null=True)
    aparente_g_cm3_field = models.FloatField(db_column='APARENTE{g/cm3}', blank=True,
                                             null=True)
    fosforo_disponible = models.FloatField(db_column='FÓSFORO DISPONIBLE', blank=True,
                                           null=True)
    porosidad_total_percentage_field = models.FloatField(db_column='Porosidad Total {Percentage}', blank=True,
                                                         null=True)

    class Meta:
        # managed = False
        db_table = 'bdl_detallada_filtrada'
        verbose_name = 'BDL Detallada'
        verbose_name_plural = '3. BDL Detallada'

    def __str__(self):
        return f"{self.horizontes}"

    def __unicode__(self):
        return f"{self.horizontes}"


class Coordenadas(models.Model):
    index = models.AutoField(primary_key=True, db_column='index')
    cod_perfil = models.OneToOneField(BdpGeneralFiltrada, on_delete=models.CASCADE, db_column='COD_PERFIL')
    latitud = models.FloatField(db_column='LATITUD')
    longitud = models.FloatField(db_column='LONGITUD')

    class Meta:
        # managed = False
        db_table = 'coordenadas'
        verbose_name = 'Coordenadas'
        verbose_name_plural = '4. Coordenadas'

    def __str__(self):
        return f"{self.cod_perfil}"

    def __unicode__(self):
        return f"{self.cod_perfil}"
