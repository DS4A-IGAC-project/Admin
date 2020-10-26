from django.db import models


class BdlDetallada(models.Model):
    id = models.AutoField(primary_key=True)
    memoria = models.TextField(db_column='MEMORIA', blank=True, null=True)  # Field name made lowercase.
    cod_perfil = models.TextField(db_column='COD_PERFIL', blank=True, null=True)  # Field name made lowercase.
    cod_perfil_hor = models.TextField(db_column='COD_PERFIL_HOR', blank=True, null=True)  # Field name made lowercase.
    longitud = models.TextField(db_column='Longitud', blank=True, null=True)  # Field name made lowercase.
    latitud = models.TextField(db_column='Latitud', blank=True, null=True)  # Field name made lowercase.
    horizonte = models.TextField(db_column='Horizonte', blank=True,
                                 null=True)  # Field name made lowercase. This field type is a guess.
    profundidad_inicial = models.TextField(db_column='Profundidad_Inicial', blank=True,
                                           null=True)  # Field name made lowercase.
    profundidad_final = models.TextField(db_column='Profundidad_Final', blank=True,
                                         null=True)  # Field name made lowercase.
    profundidades = models.TextField(db_column='Profundidades', blank=True, null=True)  # Field name made lowercase.
    boy_arena_field = models.TextField(db_column='BOY_ARENA_%', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boy_limo_field = models.TextField(db_column='BOY_LIMO_%', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boy_arcilla_field = models.TextField(db_column='BOY_ARCILLA_%', blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boy_clase_textural_field = models.TextField(db_column='BOY_CLASE_TEXTURAL_%', blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boy_gravilla_field = models.TextField(db_column='BOY_GRAVILLA_%', blank=True,
                                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ph_1_1_field = models.TextField(db_column='pH (1:1)', blank=True,
                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ph_1_5_field = models.TextField(db_column='pH (1:5)', blank=True,
                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    carbono_total = models.TextField(db_column='CARBONO TOTAL', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    carbono_organico_co_field = models.TextField(db_column='CARBONO ORGANICO (CO %)', blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    materia_organica_mo_field = models.TextField(db_column='MATERIA_ORGANICA (MO%)', blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    nitrogeno_total_field = models.TextField(db_column='NITROGENO TOTAL %', blank=True,
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fosforo_disponible = models.TextField(db_column='FOSFORO DISPONIBLE', blank=True,
                                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cica = models.TextField(db_column='CICA', blank=True, null=True)  # Field name made lowercase.
    cice = models.TextField(db_column='CICE', blank=True, null=True)  # Field name made lowercase.
    cicv = models.TextField(db_column='CICV', blank=True, null=True)  # Field name made lowercase.
    ca = models.TextField(db_column='Ca', blank=True, null=True)  # Field name made lowercase.
    mg = models.TextField(db_column='Mg', blank=True, null=True)  # Field name made lowercase.
    k = models.TextField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    na = models.TextField(db_column='Na', blank=True, null=True)  # Field name made lowercase.
    b_t_field = models.TextField(db_column='B.T.', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    acidez_intercambiable_cmol_kg = models.TextField(db_column='ACIDEZ INTERCAMBIABLE cmol(+)/Kg', blank=True,
                                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    s_a_i_field = models.TextField(db_column='S.A.I. %', blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    s_bases_field = models.TextField(db_column='S.BASES%', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    s_be_field = models.TextField(db_column='S.BE%', blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ce_ds_m_field = models.TextField(db_column='CE_(dS/m)', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    caco3_cual = models.TextField(db_column='CaCO3_CUAL', blank=True, null=True)  # Field name made lowercase.
    carbonato_de_calcio_cuantitativo = models.TextField(db_column='Carbonato de Calcio Cuantitativo', blank=True,
                                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mn_mg_kg_field = models.TextField(db_column='Mn (mg/kg)', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fe_mg_kg_field = models.TextField(db_column='Fe  (mg/kg)', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    zn_mg_kg_field = models.TextField(db_column='Zn (mg/kg)', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cu_mg_kg_field = models.TextField(db_column='Cu (mg/kg)', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    b_mg_kg_field = models.TextField(db_column='B (mg/kg)', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    s_mg_kg_field = models.TextField(db_column='S (mg/Kg)', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    aluminio_activo_field = models.TextField(db_column='ALUMINIO ACTIVO %', blank=True,
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hierro_activo_field = models.TextField(db_column='HIERRO ACTIVO %', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    retencion_fosforica_field = models.TextField(db_column='RETENCION FOSFORICA %', blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indice_melanico = models.TextField(db_column='INDICE MELANICO', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salinidad_ce_ds_m_field = models.TextField(db_column='SALINIDAD_CE_(dS/m)', blank=True,
                                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salinidad_ph = models.TextField(db_column='SALINIDAD_pH', blank=True, null=True)  # Field name made lowercase.
    salinidad_ras = models.TextField(db_column='SALINIDAD_RAS', blank=True, null=True)  # Field name made lowercase.
    salinidad_psi = models.TextField(db_column='SALINIDAD_PSI', blank=True, null=True)  # Field name made lowercase.
    salinidad_clase = models.TextField(db_column='SALINIDAD_CLASE', blank=True, null=True)  # Field name made lowercase.
    salinidad_calcio_mmol_l_field = models.TextField(db_column='SALINIDAD_CALCIO (mmol(+)/L)', blank=True,
                                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salinidad_magnesi_mmol_l_o = models.TextField(db_column='SALINIDAD_MAGNESI (mmol(+)/L)O', blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salinidad_potasio_mmol_l_field = models.TextField(db_column='SALINIDAD_POTASIO (mmol(+)/L)', blank=True,
                                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salinidad_sodio_mmol_l_field = models.TextField(db_column='SALINIDAD_SODIO (mmol(+)/L)', blank=True,
                                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salinidad_hierro_mmol_l_field = models.TextField(db_column='SALINIDAD_HIERRO (mmol(+)/L)', blank=True,
                                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salinidad_amonio_mmol_l_field = models.TextField(db_column='SALINIDAD_AMONIO (mmol(+)/L)', blank=True,
                                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salinidad_suma_cationes_mmol_l_field = models.TextField(db_column='SALINIDAD_SUMA CATIONES (mmol(+)/L)', blank=True,
                                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salinidad_pa_field = models.TextField(db_column='SALINIDAD_Pa(%)', blank=True,
                                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salinidad_cic_cmol_kg_field = models.TextField(db_column='SALINIDAD_CIC (cmol(+)/Kg)', blank=True,
                                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salinidad_na_inter_real_cmol_kg_field = models.TextField(db_column='SALINIDAD_Na Inter Real (cmol(+)/Kg)',
                                                             blank=True,
                                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    aparente_g_cm3_field = models.TextField(db_column='APARENTE(g/cm3)', blank=True,
                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    real_g_cm3_field = models.TextField(db_column='REAL (g/cm3)', blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_0_kpa_field = models.TextField(db_column='_0(kPa)', blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_33_kpa_field = models.TextField(db_column='-33(kPa)', blank=True,
                                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_100_kpa_field = models.TextField(db_column='-100(kPa)', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_500_kpa_field = models.TextField(db_column='-500(kPa)', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_1000_kpa_field = models.TextField(db_column='-1000(kPa)', blank=True,
                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_1500_kpa_field = models.TextField(db_column='-1500(kPa)', blank=True,
                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    humedad_aprovechable_field = models.TextField(db_column='Humedad Aprovechable (%)', blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    porosidad_total_field = models.TextField(db_column='Porosidad Total (%)', blank=True,
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    macroporosidad_field = models.TextField(db_column='Macroporosidad (%)', blank=True,
                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    microporosidad_field = models.TextField(db_column='Microporosidad (%)', blank=True,
                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    grava_field = models.TextField(db_column='GRAVA (%)', blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_2_1_mm_field = models.TextField(db_column='_2 - 1 (mm)', blank=True,
                                          null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_1_0_5_mm_field = models.TextField(db_column='_1 - 0,5 (mm)', blank=True,
                                            null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_0_5_0_25_mm_field = models.TextField(db_column='_0,5 - 0,25 (mm)', blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_0_25_0_1_mm_field = models.TextField(db_column='_0,25 - 0,1 (mm)', blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_0_1_0_05_mm_field = models.TextField(db_column='_0,1 - 0,05 (mm)', blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_0_05_0_02_mm_field = models.TextField(db_column='_0,05 - 0,02 (mm)', blank=True,
                                                null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_0_02_0_002_mm_field = models.TextField(db_column='_0,02 - 0,002 (mm)', blank=True,
                                                 null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_0_002_mm_field = models.TextField(db_column='<0,002 (mm)', blank=True,
                                            null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    arena_field = models.TextField(db_column='ARENA (%)', blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    limo_field = models.TextField(db_column='LIMO (%)', blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    arcilla_field = models.TextField(db_column='ARCILLA (%)', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    clase_textural = models.TextField(db_column='Clase Textural', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    limite_liquido = models.TextField(db_column='Limite Liquido', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    limite_plastico = models.TextField(db_column='Limite Plastico', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indice_de_plasticidad = models.TextField(db_column='Indice de Plasticidad', blank=True,
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_de_tamizado = models.TextField(db_column='TIPO DE TAMIZADO', blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seco_8_a_6_3_mm = models.TextField(db_column='Seco 8 a 6,3 mm', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seco_6_3_a_4_mm = models.TextField(db_column='Seco 6,3 a 4 mm', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seco_4_a_2_mm = models.TextField(db_column='Seco 4 a 2 mm', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seco_2_a_1_mm = models.TextField(db_column='Seco 2 a 1 mm', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seco_1_a_0_425_mm = models.TextField(db_column='Seco 1 a 0,425 mm', blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seco_0_425_mm = models.TextField(db_column='Seco 0,425 mm', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    humedo_8_a_6_3_mm = models.TextField(db_column='Humedo 8 a 6,3 mm', blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    humedo_6_3_a_4_mm = models.TextField(db_column='Humedo 6,3 a 4 mm', blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    humedo_4_a_2_mm = models.TextField(db_column='Humedo 4 a 2 mm', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    humedo_2_a_1_mm = models.TextField(db_column='Humedo 2 a 1 mm', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    humedo_1_a_0_425_mm = models.TextField(db_column='Humedo 1 a 0,425 mm', blank=True,
                                           null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    humedo_0_425_mm = models.TextField(db_column='Humedo 0,425 mm', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indice_de_agregacion = models.TextField(db_column='Indice de Agregacion', blank=True,
                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diametro_ponderado_medio_d_p_m_field = models.TextField(db_column='Diametro ponderado medio (D.P.M.)', blank=True,
                                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    calific_dpm = models.TextField(db_column='CALIFIC_DPM', blank=True, null=True)  # Field name made lowercase.
    cole = models.TextField(db_column='COLE', blank=True, null=True)  # Field name made lowercase.
    calific_cole = models.TextField(db_column='CALIFIC_COLE', blank=True, null=True)  # Field name made lowercase.
    arena_aglomerados = models.TextField(db_column='Arena_Aglomerados', blank=True,
                                         null=True)  # Field name made lowercase.
    arena_agregados = models.TextField(db_column='Arena_Agregados', blank=True, null=True)  # Field name made lowercase.
    arena_alterados = models.TextField(db_column='Arena_Alterados', blank=True, null=True)  # Field name made lowercase.
    arena_amorfo = models.TextField(db_column='Arena_Amorfo', blank=True, null=True)  # Field name made lowercase.
    arena_andalucita = models.TextField(db_column='Arena_Andalucita', blank=True,
                                        null=True)  # Field name made lowercase.
    arena_anfiboles = models.TextField(db_column='Arena_Anfiboles', blank=True, null=True)  # Field name made lowercase.
    arena_apatito = models.TextField(db_column='Arena_Apatito', blank=True, null=True)  # Field name made lowercase.
    arena_bayerita = models.TextField(db_column='Arena_Bayerita', blank=True, null=True)  # Field name made lowercase.
    arena_biotita = models.TextField(db_column='Arena_Biotita', blank=True, null=True)  # Field name made lowercase.
    arena_bormerita = models.TextField(db_column='Arena_Bormerita', blank=True, null=True)  # Field name made lowercase.
    arena_broquita = models.TextField(db_column='Arena_Broquita', blank=True, null=True)  # Field name made lowercase.
    arena_calcita = models.TextField(db_column='Arena_Calcita', blank=True, null=True)  # Field name made lowercase.
    arena_caolinita = models.TextField(db_column='Arena_Caolinita', blank=True, null=True)  # Field name made lowercase.
    arena_carbonatos = models.TextField(db_column='Arena_Carbonatos', blank=True,
                                        null=True)  # Field name made lowercase.
    arena_circon = models.TextField(db_column='Arena_Circon', blank=True, null=True)  # Field name made lowercase.
    arena_clorita = models.TextField(db_column='Arena_Clorita', blank=True, null=True)  # Field name made lowercase.
    arena_cristobalita = models.TextField(db_column='Arena_Cristobalita', blank=True,
                                          null=True)  # Field name made lowercase.
    arena_cuarzo = models.TextField(db_column='Arena_Cuarzo', blank=True, null=True)  # Field name made lowercase.
    arena_desconocida = models.TextField(db_column='Arena_Desconocida', blank=True,
                                         null=True)  # Field name made lowercase.
    arena_diopsido = models.TextField(db_column='Arena_Diopsido', blank=True, null=True)  # Field name made lowercase.
    arena_epidota = models.TextField(db_column='Arena_Epidota', blank=True, null=True)  # Field name made lowercase.
    arena_feldespatos = models.TextField(db_column='Arena_Feldespatos', blank=True,
                                         null=True)  # Field name made lowercase.
    arena_fitolitos_de_opalo = models.TextField(db_column='Arena_Fitolitos de Opalo', blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_fitolitos = models.TextField(db_column='Arena_Fitolitos', blank=True, null=True)  # Field name made lowercase.
    arena_fluorita = models.TextField(db_column='Arena_Fluorita', blank=True, null=True)  # Field name made lowercase.
    arena_fragmentos_carbonosos_organicos = models.TextField(db_column='Arena_Fragmentos Carbonosos Organicos',
                                                             blank=True,
                                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_fragmentos_de_roca = models.TextField(db_column='Arena_Fragmentos de Roca', blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_fragmentos_tobaceos = models.TextField(db_column='Arena_Fragmentos Tobaceos', blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_gibsita = models.TextField(db_column='Arena_Gibsita', blank=True, null=True)  # Field name made lowercase.
    arena_glaucofana = models.TextField(db_column='Arena_Glaucofana', blank=True,
                                        null=True)  # Field name made lowercase.
    arena_goetita = models.TextField(db_column='Arena_Goetita', blank=True, null=True)  # Field name made lowercase.
    arena_granate = models.TextField(db_column='Arena_Granate', blank=True, null=True)  # Field name made lowercase.
    arena_granos_alterados = models.TextField(db_column='Arena_Granos alterados', blank=True,
                                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_haloisita = models.TextField(db_column='Arena_Haloisita', blank=True, null=True)  # Field name made lowercase.
    arena_hematita = models.TextField(db_column='Arena_Hematita', blank=True, null=True)  # Field name made lowercase.
    arena_hiperstena = models.TextField(db_column='Arena_Hiperstena', blank=True,
                                        null=True)  # Field name made lowercase.
    arena_hornblenda = models.TextField(db_column='Arena_Hornblenda', blank=True,
                                        null=True)  # Field name made lowercase.
    arena_ilita = models.TextField(db_column='Arena_Ilita', blank=True, null=True)  # Field name made lowercase.
    arena_interestratificados = models.TextField(db_column='Arena_Interestratificados', blank=True,
                                                 null=True)  # Field name made lowercase.
    arena_intergrados = models.TextField(db_column='Arena_Intergrados', blank=True,
                                         null=True)  # Field name made lowercase.
    arena_lamprobolita = models.TextField(db_column='Arena_Lamprobolita', blank=True,
                                          null=True)  # Field name made lowercase.
    arena_lepidocrocita = models.TextField(db_column='Arena_Lepidocrocita', blank=True,
                                           null=True)  # Field name made lowercase.
    arena_leucoxeno = models.TextField(db_column='Arena_Leucoxeno', blank=True, null=True)  # Field name made lowercase.
    arena_maficas = models.TextField(db_column='Arena_Maficas', blank=True, null=True)  # Field name made lowercase.
    arena_magnetita = models.TextField(db_column='Arena_Magnetita', blank=True, null=True)  # Field name made lowercase.
    arena_material_alofanico = models.TextField(db_column='Arena_Material Alofanico', blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_materiales_amorfos = models.TextField(db_column='Arena_Materiales Amorfos', blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_metahaloicita_field = models.TextField(db_column='Arena_Metahaloicita ', blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    arena_micas = models.TextField(db_column='Arena_Micas', blank=True, null=True)  # Field name made lowercase.
    arena_minerales_densos = models.TextField(db_column='Arena_Minerales densos', blank=True,
                                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_minerales_livianos = models.TextField(db_column='Arena_Minerales livianos', blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_montmorillonita_esmectitas_field = models.TextField(db_column='Arena_Montmorillonita (Esmectitas)',
                                                              blank=True,
                                                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    arena_muscovita = models.TextField(db_column='Arena_Muscovita', blank=True, null=True)  # Field name made lowercase.
    arena_no_determinado = models.TextField(db_column='Arena_No determinado', blank=True,
                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_opacos = models.TextField(db_column='Arena_Opacos', blank=True, null=True)  # Field name made lowercase.
    arena_ortopirita = models.TextField(db_column='Arena_Ortopirita', blank=True,
                                        null=True)  # Field name made lowercase.
    arena_oxidos = models.TextField(db_column='Arena_Oxidos', blank=True, null=True)  # Field name made lowercase.
    arena_oxidos_de_hierro = models.TextField(db_column='Arena_Oxidos de Hierro', blank=True,
                                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_pirofilita = models.TextField(db_column='Arena_Pirofilita', blank=True,
                                        null=True)  # Field name made lowercase.
    arena_piroxenos = models.TextField(db_column='Arena_Piroxenos', blank=True, null=True)  # Field name made lowercase.
    arena_plagioclasas = models.TextField(db_column='Arena_Plagioclasas', blank=True,
                                          null=True)  # Field name made lowercase.
    arena_productos_sesquioxidos = models.TextField(db_column='Arena_Productos Sesquioxidos', blank=True,
                                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_rutilo = models.TextField(db_column='Arena_Rutilo', blank=True, null=True)  # Field name made lowercase.
    arena_sustancias_no_cristalinas = models.TextField(db_column='Arena_Sustancias no Cristalinas', blank=True,
                                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_talco = models.TextField(db_column='Arena_Talco', blank=True, null=True)  # Field name made lowercase.
    arena_titanita = models.TextField(db_column='Arena_Titanita', blank=True, null=True)  # Field name made lowercase.
    arena_turmalina = models.TextField(db_column='Arena_Turmalina', blank=True, null=True)  # Field name made lowercase.
    arena_vermiculita = models.TextField(db_column='Arena_Vermiculita', blank=True,
                                         null=True)  # Field name made lowercase.
    arena_vidrio_volcanico = models.TextField(db_column='Arena_Vidrio Volcanico', blank=True,
                                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arena_zoisita = models.TextField(db_column='Arena_Zoisita', blank=True, null=True)  # Field name made lowercase.
    arcilla_amorfos = models.TextField(db_column='Arcilla_Amorfos', blank=True, null=True)  # Field name made lowercase.
    arcilla_anfiboles = models.TextField(db_column='Arcilla_Anfiboles', blank=True,
                                         null=True)  # Field name made lowercase.
    arcilla_biotita = models.TextField(db_column='Arcilla_Biotita', blank=True, null=True)  # Field name made lowercase.
    arcilla_calcita = models.TextField(db_column='Arcilla_Calcita', blank=True, null=True)  # Field name made lowercase.
    arcilla_caolinita = models.TextField(db_column='Arcilla_Caolinita', blank=True,
                                         null=True)  # Field name made lowercase.
    arcilla_clorita = models.TextField(db_column='Arcilla_Clorita', blank=True, null=True)  # Field name made lowercase.
    arcilla_cristobalita = models.TextField(db_column='Arcilla_Cristobalita', blank=True,
                                            null=True)  # Field name made lowercase.
    arcilla_cuarzo = models.TextField(db_column='Arcilla_Cuarzo', blank=True, null=True)  # Field name made lowercase.
    arcilla_dolomita = models.TextField(db_column='Arcilla_Dolomita', blank=True,
                                        null=True)  # Field name made lowercase.
    arcilla_epidotita = models.TextField(db_column='Arcilla_Epidotita', blank=True,
                                         null=True)  # Field name made lowercase.
    arcilla_esmectita = models.TextField(db_column='Arcilla_Esmectita', blank=True,
                                         null=True)  # Field name made lowercase.
    arcilla_feldespatos = models.TextField(db_column='Arcilla_Feldespatos', blank=True,
                                           null=True)  # Field name made lowercase.
    arcilla_fitolitos_de_opalo = models.TextField(db_column='Arcilla_Fitolitos de Opalo', blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arcilla_gibsita = models.TextField(db_column='Arcilla_Gibsita', blank=True, null=True)  # Field name made lowercase.
    arcilla_goetita = models.TextField(db_column='Arcilla_Goetita', blank=True, null=True)  # Field name made lowercase.
    arcilla_halita = models.TextField(db_column='Arcilla_Halita', blank=True, null=True)  # Field name made lowercase.
    arcilla_haloisita = models.TextField(db_column='Arcilla_Haloisita', blank=True,
                                         null=True)  # Field name made lowercase.
    arcilla_hematita = models.TextField(db_column='Arcilla_Hematita', blank=True,
                                        null=True)  # Field name made lowercase.
    arcilla_hidromicas = models.TextField(db_column='Arcilla_Hidromicas', blank=True,
                                          null=True)  # Field name made lowercase.
    arcilla_ilita = models.TextField(db_column='Arcilla_Ilita', blank=True, null=True)  # Field name made lowercase.
    arcilla_interestratificados = models.TextField(db_column='Arcilla_Interestratificados', blank=True,
                                                   null=True)  # Field name made lowercase.
    arcilla_intergrados_2_1_2_2 = models.TextField(db_column='Arcilla_Intergrados 2:1-2:2', blank=True,
                                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arcilla_lepidocrocita = models.TextField(db_column='Arcilla_Lepidocrocita', blank=True,
                                             null=True)  # Field name made lowercase.
    arcilla_maficas = models.TextField(db_column='Arcilla_Maficas', blank=True, null=True)  # Field name made lowercase.
    arcilla_material_alofanico = models.TextField(db_column='Arcilla_Material Alofanico', blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arcilla_material_no_cristalino = models.TextField(db_column='Arcilla_Material no cristalino', blank=True,
                                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arcilla_materiales_amorfos = models.TextField(db_column='Arcilla_Materiales Amorfos', blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arcilla_metahaloisita = models.TextField(db_column='Arcilla_Metahaloisita', blank=True,
                                             null=True)  # Field name made lowercase.
    arcilla_micas = models.TextField(db_column='Arcilla_Micas', blank=True, null=True)  # Field name made lowercase.
    arcilla_minerales_livianos = models.TextField(db_column='Arcilla_Minerales livianos', blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arcilla_montmorillonita_esmectitas_field = models.TextField(db_column='Arcilla_Montmorillonita (Esmectitas)',
                                                                blank=True,
                                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    arcilla_muscovita = models.TextField(db_column='Arcilla_Muscovita', blank=True,
                                         null=True)  # Field name made lowercase.
    arcilla_opacos = models.TextField(db_column='Arcilla_Opacos', blank=True, null=True)  # Field name made lowercase.
    arcilla_oxidos = models.TextField(db_column='Arcilla_Oxidos', blank=True, null=True)  # Field name made lowercase.
    arcilla_pirofilita = models.TextField(db_column='Arcilla_Pirofilita', blank=True,
                                          null=True)  # Field name made lowercase.
    arcilla_plagioclasas = models.TextField(db_column='Arcilla_Plagioclasas', blank=True,
                                            null=True)  # Field name made lowercase.
    arcilla_sin_dato = models.TextField(db_column='Arcilla_Sin dato', blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arcilla_sustancias_no_cristalinas = models.TextField(db_column='Arcilla_Sustancias no Cristalinas', blank=True,
                                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arcilla_talco = models.TextField(db_column='Arcilla_Talco', blank=True, null=True)  # Field name made lowercase.
    arcilla_vermiculita = models.TextField(db_column='Arcilla_Vermiculita', blank=True,
                                           null=True)  # Field name made lowercase.
    arcilla_vidrio_volcanico = models.TextField(db_column='Arcilla_Vidrio Volcanico', blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arcilla_yeso = models.TextField(db_column='Arcilla_Yeso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bdl_detallada'


class BdpDetallada(models.Model):
    id = models.AutoField(primary_key=True)
    departamento = models.TextField(db_column='DEPARTAMENTO', blank=True, null=True)  # Field name made lowercase.
    horizontes = models.TextField(db_column='HORIZONTES', blank=True, null=True)  # Field name made lowercase.
    cod_perfil = models.TextField(db_column='COD_PERFIL', blank=True, null=True)  # Field name made lowercase.
    edafologo = models.TextField(db_column='EDAFOLOGO', blank=True, null=True)  # Field name made lowercase.
    tipo_perfil = models.TextField(db_column='TIPO_PERFIL', blank=True, null=True)  # Field name made lowercase.
    categoria_perfil = models.TextField(db_column='CATEGORIA_PERFIL', blank=True,
                                        null=True)  # Field name made lowercase.
    estudio_origen = models.TextField(db_column='ESTUDIO_ORIGEN', blank=True, null=True)  # Field name made lowercase.
    fecha = models.TextField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    simbolo_ucs = models.TextField(db_column='SIMBOLO_UCS', blank=True, null=True)  # Field name made lowercase.
    tipo_ucs = models.TextField(db_column='TIPO_UCS', blank=True, null=True)  # Field name made lowercase.
    departamento_1 = models.TextField(db_column='DEPARTAMENTO.1', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cod_depto = models.BigIntegerField(db_column='COD_DEPTO', blank=True, null=True)  # Field name made lowercase.
    municipio = models.TextField(db_column='MUNICIPIO', blank=True, null=True)  # Field name made lowercase.
    sitio = models.TextField(db_column='SITIO', blank=True, null=True)  # Field name made lowercase.
    clima_ambiental = models.TextField(db_column='CLIMA_AMBIENTAL', blank=True, null=True)  # Field name made lowercase.
    paisaje = models.TextField(db_column='PAISAJE', blank=True, null=True)  # Field name made lowercase.
    tipo_relieve = models.TextField(db_column='TIPO_RELIEVE', blank=True, null=True)  # Field name made lowercase.
    forma_terreno = models.TextField(db_column='FORMA_TERRENO', blank=True, null=True)  # Field name made lowercase.
    material_parental_litologia = models.TextField(db_column='MATERIAL_PARENTAL_LITOLOGIA', blank=True,
                                                   null=True)  # Field name made lowercase.
    grado_alteracion_mp = models.TextField(db_column='GRADO_ALTERACION_MP', blank=True,
                                           null=True)  # Field name made lowercase.
    clase_pendiente = models.TextField(db_column='CLASE_PENDIENTE', blank=True, null=True)  # Field name made lowercase.
    diseccion = models.TextField(db_column='DISECCION', blank=True, null=True)  # Field name made lowercase.
    microrelieve = models.TextField(db_column='MICRORELIEVE', blank=True, null=True)  # Field name made lowercase.
    porc_pendiente = models.TextField(db_column='PORC_PENDIENTE', blank=True, null=True)  # Field name made lowercase.
    longitud_pendiente = models.TextField(db_column='LONGITUD_PENDIENTE', blank=True,
                                          null=True)  # Field name made lowercase.
    forma_pendiente = models.TextField(db_column='FORMA_PENDIENTE', blank=True, null=True)  # Field name made lowercase.
    formacion_ecologica = models.TextField(db_column='FORMACION_ECOLOGICA', blank=True,
                                           null=True)  # Field name made lowercase.
    t_prom_anual = models.TextField(db_column='T_PROM_ANUAL', blank=True, null=True)  # Field name made lowercase.
    precipitacion_prom_anual = models.TextField(db_column='PRECIPITACION_PROM_ANUAL', blank=True,
                                                null=True)  # Field name made lowercase.
    distribucion_lluvias = models.TextField(db_column='DISTRIBUCION_LLUVIAS', blank=True,
                                            null=True)  # Field name made lowercase.
    regimen_temperatura = models.TextField(db_column='REGIMEN_TEMPERATURA', blank=True,
                                           null=True)  # Field name made lowercase.
    regimen_humedad = models.TextField(db_column='REGIMEN_HUMEDAD', blank=True, null=True)  # Field name made lowercase.
    clase_degradacion = models.TextField(db_column='CLASE_DEGRADACION', blank=True,
                                         null=True)  # Field name made lowercase.
    tipo_degradacion = models.TextField(db_column='TIPO_DEGRADACION', blank=True,
                                        null=True)  # Field name made lowercase.
    clase_erosion = models.TextField(db_column='CLASE_EROSION', blank=True, null=True)  # Field name made lowercase.
    tipo_erosion = models.TextField(db_column='TIPO_EROSION', blank=True, null=True)  # Field name made lowercase.
    grado_erosion = models.TextField(db_column='GRADO_EROSION', blank=True, null=True)  # Field name made lowercase.
    evidencias_erosion = models.TextField(db_column='EVIDENCIAS_EROSION', blank=True,
                                          null=True)  # Field name made lowercase.
    clase_movimiento_masa = models.TextField(db_column='CLASE_MOVIMIENTO_MASA', blank=True,
                                             null=True)  # Field name made lowercase.
    tipo_movimiento_masa = models.TextField(db_column='TIPO_MOVIMIENTO_MASA', blank=True,
                                            null=True)  # Field name made lowercase.
    frecuencia_movimiento_masa = models.TextField(db_column='FRECUENCIA_MOVIMIENTO_MASA', blank=True,
                                                  null=True)  # Field name made lowercase.
    drenaje_interno = models.TextField(db_column='DRENAJE_INTERNO', blank=True, null=True)  # Field name made lowercase.
    drenaje_externo = models.TextField(db_column='DRENAJE_EXTERNO', blank=True, null=True)  # Field name made lowercase.
    drenaje_natural = models.TextField(db_column='DRENAJE_NATURAL', blank=True, null=True)  # Field name made lowercase.
    nivel_freatico = models.TextField(db_column='NIVEL_FREATICO', blank=True, null=True)  # Field name made lowercase.
    prof_nivel_freaticocm = models.TextField(db_column='PROF_NIVEL_FREATICOcm', blank=True,
                                             null=True)  # Field name made lowercase.
    profundidad_efectiva = models.TextField(db_column='PROFUNDIDAD_EFECTIVA', blank=True,
                                            null=True)  # Field name made lowercase.
    limitantes_profundidad_efectiva = models.TextField(db_column='LIMITANTES_PROFUNDIDAD_EFECTIVA', blank=True,
                                                       null=True)  # Field name made lowercase.
    agente_cementante = models.TextField(db_column='AGENTE_CEMENTANTE', blank=True,
                                         null=True)  # Field name made lowercase.
    cementacion_grado = models.TextField(db_column='CEMENTACION_GRADO', blank=True,
                                         null=True)  # Field name made lowercase.
    plintita_volumen = models.TextField(db_column='PLINTITA_VOLUMEN', blank=True,
                                        null=True)  # Field name made lowercase.
    plintita_fase = models.TextField(db_column='PLINTITA_FASE', blank=True, null=True)  # Field name made lowercase.
    tipo_pedregosidad = models.TextField(db_column='TIPO_PEDREGOSIDAD', blank=True,
                                         null=True)  # Field name made lowercase.
    porc_pedregosidad_superficial_cubierta = models.TextField(db_column='PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA',
                                                              blank=True, null=True)  # Field name made lowercase.
    clase_pedregosidad = models.TextField(db_column='CLASE_PEDREGOSIDAD', blank=True,
                                          null=True)  # Field name made lowercase.
    porc_afloramiento_superficie_cubierta = models.TextField(db_column='PORC_AFLORAMIENTO_SUPERFICIE_CUBIERTA',
                                                             blank=True, null=True)  # Field name made lowercase.
    clase_afloramiento = models.TextField(db_column='CLASE_AFLORAMIENTO', blank=True,
                                          null=True)  # Field name made lowercase.
    fase_inundacion_encharcamiento = models.TextField(db_column='FASE_INUNDACION_ENCHARCAMIENTO', blank=True,
                                                      null=True)  # Field name made lowercase.
    frecuencia_inundacion = models.TextField(db_column='FRECUENCIA_INUNDACION', blank=True,
                                             null=True)  # Field name made lowercase.
    duracion_inundacion = models.TextField(db_column='DURACION_INUNDACION', blank=True,
                                           null=True)  # Field name made lowercase.
    frecuencia_encharcamiento = models.TextField(db_column='FRECUENCIA_ENCHARCAMIENTO', blank=True,
                                                 null=True)  # Field name made lowercase.
    duracion_encharcamiento = models.TextField(db_column='DURACION_ENCHARCAMIENTO', blank=True,
                                               null=True)  # Field name made lowercase.
    observaciones_horizontes = models.TextField(db_column='OBSERVACIONES_HORIZONTES', blank=True,
                                                null=True)  # Field name made lowercase.
    uso_actual = models.TextField(db_column='USO_ACTUAL', blank=True, null=True)  # Field name made lowercase.
    vegetacion_natural = models.TextField(db_column='VEGETACION_NATURAL', blank=True,
                                          null=True)  # Field name made lowercase.
    nombres_cultivos_pastos = models.TextField(db_column='NOMBRES_CULTIVOS_PASTOS', blank=True,
                                               null=True)  # Field name made lowercase.
    limitante_uso = models.TextField(db_column='LIMITANTE_USO', blank=True, null=True)  # Field name made lowercase.
    clase_clasif_agrologica = models.TextField(db_column='CLASE_CLASIF_AGROLOGICA', blank=True,
                                               null=True)  # Field name made lowercase. This field type is a guess.
    subclase_clasif_agrologica = models.TextField(db_column='SUBCLASE_CLASIF_AGROLOGICA', blank=True,
                                                  null=True)  # Field name made lowercase.
    grietas_ancho_mm = models.TextField(db_column='GRIETAS_ANCHO_mm', blank=True,
                                        null=True)  # Field name made lowercase. This field type is a guess.
    grietas_profundidad_cm = models.TextField(db_column='GRIETAS_PROFUNDIDAD_cm', blank=True,
                                              null=True)  # Field name made lowercase. This field type is a guess.
    caracteristicas_diagnosticas = models.TextField(db_column='CARACTERISTICAS_DIAGNOSTICAS', blank=True,
                                                    null=True)  # Field name made lowercase.
    epipedon = models.TextField(db_column='EPIPEDON', blank=True, null=True)  # Field name made lowercase.
    endopedon_1 = models.TextField(db_column='ENDOPEDON_1', blank=True, null=True)  # Field name made lowercase.
    endopedon_2 = models.TextField(db_column='ENDOPEDON_2', blank=True, null=True)  # Field name made lowercase.
    clasificacion_taxonomica = models.TextField(db_column='CLASIFICACION_TAXONOMICA', blank=True,
                                                null=True)  # Field name made lowercase.
    familia_textural = models.TextField(db_column='FAMILIA_TEXTURAL', blank=True,
                                        null=True)  # Field name made lowercase.
    grados_n = models.TextField(db_column='GRADOS_N', blank=True,
                                null=True)  # Field name made lowercase. This field type is a guess.
    minutos_n = models.TextField(db_column='MINUTOS_N', blank=True,
                                 null=True)  # Field name made lowercase. This field type is a guess.
    segundos_n = models.TextField(db_column='SEGUNDOS_N', blank=True, null=True)  # Field name made lowercase.
    grados_w = models.TextField(db_column='GRADOS_W', blank=True,
                                null=True)  # Field name made lowercase. This field type is a guess.
    minutos_w = models.TextField(db_column='MINUTOS_W', blank=True,
                                 null=True)  # Field name made lowercase. This field type is a guess.
    segundos_w = models.TextField(db_column='SEGUNDOS_W', blank=True, null=True)  # Field name made lowercase.
    latitud = models.TextField(db_column='LATITUD', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    longitud = models.TextField(db_column='LONGITUD', blank=True,
                                null=True)  # Field name made lowercase. This field type is a guess.
    altitud = models.TextField(db_column='ALTITUD', blank=True, null=True)  # Field name made lowercase.
    observaciones_generales = models.TextField(db_column='OBSERVACIONES_GENERALES', blank=True,
                                               null=True)  # Field name made lowercase.
    fase_desp_fam_text = models.TextField(db_column='FASE_desp_fam_text', blank=True,
                                          null=True)  # Field name made lowercase.
    nomenclatura = models.TextField(db_column='NOMENCLATURA', blank=True, null=True)  # Field name made lowercase.
    profundidad_inicial = models.TextField(db_column='PROFUNDIDAD_INICIAL', blank=True,
                                           null=True)  # Field name made lowercase.
    profundidad_final = models.TextField(db_column='PROFUNDIDAD_FINAL', blank=True,
                                         null=True)  # Field name made lowercase.
    espesor = models.TextField(db_column='ESPESOR', blank=True, null=True)  # Field name made lowercase.
    rango_profundidad = models.TextField(db_column='RANGO_PROFUNDIDAD', blank=True,
                                         null=True)  # Field name made lowercase.
    color_matriz_seco1 = models.TextField(db_column='COLOR_MATRIZ_SECO1', blank=True,
                                          null=True)  # Field name made lowercase.
    color_matriz_seco2 = models.TextField(db_column='COLOR_MATRIZ_SECO2', blank=True,
                                          null=True)  # Field name made lowercase.
    porc_observado_seco2 = models.TextField(db_column='PORC_OBSERVADO_SECO2', blank=True,
                                            null=True)  # Field name made lowercase. This field type is a guess.
    color_matriz_humedo1 = models.TextField(db_column='COLOR_MATRIZ_HUMEDO1', blank=True,
                                            null=True)  # Field name made lowercase.
    color_matriz_humedo2 = models.TextField(db_column='COLOR_MATRIZ_HUMEDO2', blank=True,
                                            null=True)  # Field name made lowercase.
    porc_observado_humedo2 = models.TextField(db_column='PORC_OBSERVADO_HUMEDO2', blank=True,
                                              null=True)  # Field name made lowercase.
    motead_color = models.TextField(db_column='MOTEAD_COLOR', blank=True, null=True)  # Field name made lowercase.
    motead_cantidad = models.TextField(db_column='MOTEAD_CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    motead_tamano = models.TextField(db_column='MOTEAD_TAMANO', blank=True, null=True)  # Field name made lowercase.
    motead_nitidez = models.TextField(db_column='MOTEAD_NITIDEZ', blank=True, null=True)  # Field name made lowercase.
    motead_color_2 = models.TextField(db_column='MOTEAD_COLOR_2', blank=True, null=True)  # Field name made lowercase.
    motead_cantidad_2 = models.TextField(db_column='MOTEAD_CANTIDAD_2', blank=True,
                                         null=True)  # Field name made lowercase.
    motead_tamano_2 = models.TextField(db_column='MOTEAD_TAMANO_2', blank=True, null=True)  # Field name made lowercase.
    motead_nitidez_2 = models.TextField(db_column='MOTEAD_NITIDEZ_2', blank=True,
                                        null=True)  # Field name made lowercase.
    textura = models.TextField(db_column='TEXTURA', blank=True, null=True)  # Field name made lowercase.
    modificador_textura = models.TextField(db_column='MODIFICADOR_TEXTURA', blank=True,
                                           null=True)  # Field name made lowercase.
    tipo_fr_1 = models.TextField(db_column='TIPO_FR_1', blank=True, null=True)  # Field name made lowercase.
    forma_fr_1 = models.TextField(db_column='FORMA_FR_1', blank=True, null=True)  # Field name made lowercase.
    naturaleza_fr_1 = models.TextField(db_column='NATURALEZA_FR_1', blank=True, null=True)  # Field name made lowercase.
    volumen_por_cfr_1 = models.TextField(db_column='VOLUMEN_POR_CFR_1', blank=True,
                                         null=True)  # Field name made lowercase.
    tipo_fr_2 = models.TextField(db_column='TIPO_FR_2', blank=True, null=True)  # Field name made lowercase.
    forma_fr_2 = models.TextField(db_column='FORMA_FR_2', blank=True, null=True)  # Field name made lowercase.
    naturaleza_fr_2 = models.TextField(db_column='NATURALEZA_FR_2', blank=True,
                                       null=True)  # Field name made lowercase. This field type is a guess.
    volumen_por_cfr_2 = models.TextField(db_column='VOLUMEN_POR_CFR_2', blank=True,
                                         null=True)  # Field name made lowercase. This field type is a guess.
    tipo_fr_3 = models.TextField(db_column='TIPO_FR_3', blank=True, null=True)  # Field name made lowercase.
    forma_fr_3 = models.TextField(db_column='FORMA_FR_3', blank=True, null=True)  # Field name made lowercase.
    naturaleza_fr_3 = models.TextField(db_column='NATURALEZA_FR_3', blank=True,
                                       null=True)  # Field name made lowercase. This field type is a guess.
    volumen_por_cfr_3 = models.TextField(db_column='VOLUMEN_POR_CFR_3', blank=True,
                                         null=True)  # Field name made lowercase. This field type is a guess.
    volumen_porcfr = models.TextField(db_column='VOLUMEN[?]_PORCFR', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    clase_s_org = models.TextField(db_column='CLASE_S_ORG', blank=True, null=True)  # Field name made lowercase.
    composicion_s_org = models.TextField(db_column='COMPOSICION_S_ORG', blank=True,
                                         null=True)  # Field name made lowercase.
    tipo_estructura_1 = models.TextField(db_column='TIPO_ESTRUCTURA_1', blank=True,
                                         null=True)  # Field name made lowercase.
    clase_estructura_1 = models.TextField(db_column='CLASE_ESTRUCTURA_1', blank=True,
                                          null=True)  # Field name made lowercase.
    grado_estructura = models.TextField(db_column='GRADO_ESTRUCTURA', blank=True,
                                        null=True)  # Field name made lowercase.
    consistencia_seco = models.TextField(db_column='CONSISTENCIA_SECO', blank=True,
                                         null=True)  # Field name made lowercase.
    consistencia_humedo = models.TextField(db_column='CONSISTENCIA_HUMEDO', blank=True,
                                           null=True)  # Field name made lowercase.
    consist_mojado_pegj = models.TextField(db_column='CONSIST_MOJADO_PEGJ', blank=True,
                                           null=True)  # Field name made lowercase.
    consist_mojado_pl = models.TextField(db_column='CONSIST_MOJADO_PL', blank=True,
                                         null=True)  # Field name made lowercase.
    aspectos_peds_1 = models.TextField(db_column='ASPECTOS_PEDS_1', blank=True, null=True)  # Field name made lowercase.
    cantidad_asp_peds_1 = models.TextField(db_column='CANTIDAD_ASP_PEDS_1', blank=True,
                                           null=True)  # Field name made lowercase.
    claridad_asp_peds_1 = models.TextField(db_column='CLARIDAD_ASP_PEDS_1', blank=True,
                                           null=True)  # Field name made lowercase.
    localiz_asp_peds_1 = models.TextField(db_column='LOCALIZ_ASP_PEDS_1', blank=True,
                                          null=True)  # Field name made lowercase.
    aspectos_peds_2 = models.TextField(db_column='ASPECTOS_PEDS_2', blank=True, null=True)  # Field name made lowercase.
    cantidad_asp_peds_2 = models.TextField(db_column='CANTIDAD_ASP_PEDS_2', blank=True,
                                           null=True)  # Field name made lowercase.
    claridad_asp_peds_2 = models.TextField(db_column='CLARIDAD_ASP_PEDS_2', blank=True,
                                           null=True)  # Field name made lowercase.
    localiz_peds_2 = models.TextField(db_column='LOCALIZ_PEDS_2', blank=True,
                                      null=True)  # Field name made lowercase. This field type is a guess.
    cantidad_conc_1 = models.TextField(db_column='CANTIDAD_CONC_1', blank=True, null=True)  # Field name made lowercase.
    clase_conc_1 = models.TextField(db_column='CLASE_CONC_1', blank=True, null=True)  # Field name made lowercase.
    composic_conc_1 = models.TextField(db_column='COMPOSIC_CONC_1', blank=True, null=True)  # Field name made lowercase.
    forma_conc_1 = models.TextField(db_column='FORMA_CONC_1', blank=True, null=True)  # Field name made lowercase.
    tamano_conc_1 = models.TextField(db_column='TAMANO_CONC_1', blank=True, null=True)  # Field name made lowercase.
    consistencia_conc_1 = models.TextField(db_column='CONSISTENCIA_CONC_1', blank=True,
                                           null=True)  # Field name made lowercase.
    distribucion_conc_1 = models.TextField(db_column='DISTRIBUCION_CONC_1', blank=True,
                                           null=True)  # Field name made lowercase.
    cantidad_conc_2 = models.TextField(db_column='CANTIDAD_CONC_2', blank=True, null=True)  # Field name made lowercase.
    clase_conc_2 = models.TextField(db_column='CLASE_CONC_2', blank=True, null=True)  # Field name made lowercase.
    composic_conc_2 = models.TextField(db_column='COMPOSIC_CONC_2', blank=True, null=True)  # Field name made lowercase.
    forma_conc_2 = models.TextField(db_column='FORMA_CONC_2', blank=True, null=True)  # Field name made lowercase.
    tamano_conc_2 = models.TextField(db_column='TAMANO_CONC_2', blank=True, null=True)  # Field name made lowercase.
    consistencia_conc_2 = models.TextField(db_column='CONSISTENCIA_CONC_2', blank=True,
                                           null=True)  # Field name made lowercase.
    distribucion_conc_2 = models.TextField(db_column='DISTRIBUCION_CONC_2', blank=True,
                                           null=True)  # Field name made lowercase.
    cantidad_poros1 = models.TextField(db_column='CANTIDAD_POROS1', blank=True, null=True)  # Field name made lowercase.
    tamano_poros1 = models.TextField(db_column='TAMANO_POROS1', blank=True, null=True)  # Field name made lowercase.
    forma_poros1 = models.TextField(db_column='FORMA_POROS1', blank=True, null=True)  # Field name made lowercase.
    cantidad_poros2 = models.TextField(db_column='CANTIDAD_POROS2', blank=True, null=True)  # Field name made lowercase.
    tamano_poros2 = models.TextField(db_column='TAMANO_POROS2', blank=True, null=True)  # Field name made lowercase.
    forma_poros2 = models.TextField(db_column='FORMA_POROS2', blank=True, null=True)  # Field name made lowercase.
    cantidad_raices_1 = models.TextField(db_column='CANTIDAD_RAICES_1', blank=True,
                                         null=True)  # Field name made lowercase.
    tamano_raices_1 = models.TextField(db_column='TAMANO_RAICES_1', blank=True, null=True)  # Field name made lowercase.
    estado_raices_1 = models.TextField(db_column='ESTADO_RAICES_1', blank=True, null=True)  # Field name made lowercase.
    distribucion_raices_1 = models.TextField(db_column='DISTRIBUCION_RAICES_1', blank=True,
                                             null=True)  # Field name made lowercase.
    localizacion_raices_1 = models.TextField(db_column='LOCALIZACION_RAICES_1', blank=True,
                                             null=True)  # Field name made lowercase.
    cantidad_raices_2 = models.TextField(db_column='CANTIDAD_RAICES_2', blank=True,
                                         null=True)  # Field name made lowercase.
    tamano_raices_2 = models.TextField(db_column='TAMANO_RAICES_2', blank=True, null=True)  # Field name made lowercase.
    estado_raices_2 = models.TextField(db_column='ESTADO_RAICES_2', blank=True, null=True)  # Field name made lowercase.
    distribucion_raices_2 = models.TextField(db_column='DISTRIBUCION_RAICES_2', blank=True,
                                             null=True)  # Field name made lowercase.
    localizacion_raices_2 = models.TextField(db_column='LOCALIZACION_RAICES_2', blank=True,
                                             null=True)  # Field name made lowercase.
    macroorganismos_activ = models.TextField(db_column='MACROORGANISMOS_ACTIV', blank=True,
                                             null=True)  # Field name made lowercase.
    reaccion_dipyridyl = models.TextField(db_column='REACCION_DIPYRIDYL', blank=True,
                                          null=True)  # Field name made lowercase.
    reaccion_naf = models.TextField(db_column='REACCION_NaF', blank=True, null=True)  # Field name made lowercase.
    reaccion_h2o2 = models.TextField(db_column='REACCION_H2O2', blank=True, null=True)  # Field name made lowercase.
    reaccion_hcl = models.TextField(db_column='REACCION_HCl', blank=True, null=True)  # Field name made lowercase.
    nitidez = models.TextField(db_column='NITIDEZ', blank=True, null=True)  # Field name made lowercase.
    topografia = models.TextField(db_column='TOPOGRAFIA', blank=True, null=True)  # Field name made lowercase.
    metodo_ph = models.TextField(db_column='METODO_ph', blank=True, null=True)  # Field name made lowercase.
    resultado_ph = models.TextField(db_column='RESULTADO_ph', blank=True, null=True)  # Field name made lowercase.
    descripcion_horizonte = models.TextField(db_column='DESCRIPCION_HORIZONTE', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bdp_detallada'


class BdpGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    memoria = models.TextField(db_column='MEMORIA', blank=True, null=True)  # Field name made lowercase.
    edafologo = models.TextField(db_column='EDAFOLOGO', blank=True, null=True)  # Field name made lowercase.
    cod_perfil = models.TextField(db_column='COD_PERFIL', blank=True, null=True)  # Field name made lowercase.
    tipo_perfil = models.TextField(db_column='TIPO_PERFIL', blank=True, null=True)  # Field name made lowercase.
    categoria_perfil = models.TextField(db_column='CATEGORIA_PERFIL', blank=True,
                                        null=True)  # Field name made lowercase.
    estudio_origen = models.TextField(db_column='ESTUDIO_ORIGEN', blank=True, null=True)  # Field name made lowercase.
    fecha = models.TextField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    simbolo_ucs = models.TextField(db_column='SIMBOLO_UCS', blank=True, null=True)  # Field name made lowercase.
    tipo_ucs = models.TextField(db_column='TIPO_UCS', blank=True, null=True)  # Field name made lowercase.
    departamento = models.TextField(db_column='DEPARTAMENTO', blank=True, null=True)  # Field name made lowercase.
    cod_depto = models.BigIntegerField(db_column='COD_DEPTO', blank=True, null=True)  # Field name made lowercase.
    municipio = models.TextField(db_column='MUNICIPIO', blank=True, null=True)  # Field name made lowercase.
    sitio = models.TextField(db_column='SITIO', blank=True, null=True)  # Field name made lowercase.
    clima_ambiental = models.TextField(db_column='CLIMA_AMBIENTAL', blank=True, null=True)  # Field name made lowercase.
    paisaje = models.TextField(db_column='PAISAJE', blank=True, null=True)  # Field name made lowercase.
    tipo_relieve = models.TextField(db_column='TIPO_RELIEVE', blank=True, null=True)  # Field name made lowercase.
    forma_terreno = models.TextField(db_column='FORMA_TERRENO', blank=True, null=True)  # Field name made lowercase.
    material_parental_litologia = models.TextField(db_column='MATERIAL_PARENTAL_LITOLOGIA', blank=True,
                                                   null=True)  # Field name made lowercase.
    grado_alteracion_mp = models.TextField(db_column='GRADO_ALTERACION_MP', blank=True,
                                           null=True)  # Field name made lowercase.
    clase_pendiente = models.TextField(db_column='CLASE_PENDIENTE', blank=True, null=True)  # Field name made lowercase.
    diseccion = models.TextField(db_column='DISECCION', blank=True, null=True)  # Field name made lowercase.
    microrelieve = models.TextField(db_column='MICRORELIEVE', blank=True, null=True)  # Field name made lowercase.
    porc_pendiente = models.TextField(db_column='PORC_PENDIENTE', blank=True, null=True)  # Field name made lowercase.
    longitud_pendiente = models.TextField(db_column='LONGITUD_PENDIENTE', blank=True,
                                          null=True)  # Field name made lowercase.
    forma_pendiente = models.TextField(db_column='FORMA_PENDIENTE', blank=True, null=True)  # Field name made lowercase.
    formacion_ecologica = models.TextField(db_column='FORMACION_ECOLOGICA', blank=True,
                                           null=True)  # Field name made lowercase.
    t_prom_anual = models.TextField(db_column='T_PROM_ANUAL', blank=True, null=True)  # Field name made lowercase.
    precipitacion_prom_anual = models.TextField(db_column='PRECIPITACION_PROM_ANUAL', blank=True,
                                                null=True)  # Field name made lowercase.
    distribucion_lluvias = models.TextField(db_column='DISTRIBUCION_LLUVIAS', blank=True,
                                            null=True)  # Field name made lowercase.
    regimen_temperatura = models.TextField(db_column='REGIMEN_TEMPERATURA', blank=True,
                                           null=True)  # Field name made lowercase.
    regimen_humedad = models.TextField(db_column='REGIMEN_HUMEDAD', blank=True, null=True)  # Field name made lowercase.
    clase_degradacion = models.TextField(db_column='CLASE_DEGRADACION', blank=True,
                                         null=True)  # Field name made lowercase.
    tipo_degradacion = models.TextField(db_column='TIPO_DEGRADACION', blank=True,
                                        null=True)  # Field name made lowercase.
    clase_erosion = models.TextField(db_column='CLASE_EROSION', blank=True, null=True)  # Field name made lowercase.
    tipo_erosion = models.TextField(db_column='TIPO_EROSION', blank=True, null=True)  # Field name made lowercase.
    grado_erosion = models.TextField(db_column='GRADO_EROSION', blank=True, null=True)  # Field name made lowercase.
    evidencias_erosion = models.TextField(db_column='EVIDENCIAS_EROSION', blank=True,
                                          null=True)  # Field name made lowercase.
    clase_movimiento_masa = models.TextField(db_column='CLASE_MOVIMIENTO_MASA', blank=True,
                                             null=True)  # Field name made lowercase.
    tipo_movimiento_masa = models.TextField(db_column='TIPO_MOVIMIENTO_MASA', blank=True,
                                            null=True)  # Field name made lowercase.
    frecuencia_movimiento_masa = models.TextField(db_column='FRECUENCIA_MOVIMIENTO_MASA', blank=True,
                                                  null=True)  # Field name made lowercase.
    drenaje_interno = models.TextField(db_column='DRENAJE_INTERNO', blank=True, null=True)  # Field name made lowercase.
    drenaje_externo = models.TextField(db_column='DRENAJE_EXTERNO', blank=True, null=True)  # Field name made lowercase.
    drenaje_natural = models.TextField(db_column='DRENAJE_NATURAL', blank=True, null=True)  # Field name made lowercase.
    nivel_freatico = models.TextField(db_column='NIVEL_FREATICO', blank=True, null=True)  # Field name made lowercase.
    prof_nivel_freaticocm = models.TextField(db_column='PROF_NIVEL_FREATICOcm', blank=True,
                                             null=True)  # Field name made lowercase.
    profundidad_efectiva = models.TextField(db_column='PROFUNDIDAD_EFECTIVA', blank=True,
                                            null=True)  # Field name made lowercase.
    limitantes_profundidad_efectiva = models.TextField(db_column='LIMITANTES_PROFUNDIDAD_EFECTIVA', blank=True,
                                                       null=True)  # Field name made lowercase.
    agente_cementante = models.TextField(db_column='AGENTE_CEMENTANTE', blank=True,
                                         null=True)  # Field name made lowercase.
    cementacion_grado = models.TextField(db_column='CEMENTACION_GRADO', blank=True,
                                         null=True)  # Field name made lowercase.
    plintita_volumen = models.TextField(db_column='PLINTITA_VOLUMEN', blank=True,
                                        null=True)  # Field name made lowercase.
    plintita_fase = models.TextField(db_column='PLINTITA_FASE', blank=True, null=True)  # Field name made lowercase.
    tipo_pedregosidad = models.TextField(db_column='TIPO_PEDREGOSIDAD', blank=True,
                                         null=True)  # Field name made lowercase.
    porc_pedregosidad_superficial_cubierta = models.TextField(db_column='PORC_PEDREGOSIDAD_SUPERFICIAL_CUBIERTA',
                                                              blank=True, null=True)  # Field name made lowercase.
    clase_pedregosidad = models.TextField(db_column='CLASE_PEDREGOSIDAD', blank=True,
                                          null=True)  # Field name made lowercase.
    porc_afloramiento_superficie_cubierta = models.TextField(db_column='PORC_AFLORAMIENTO_SUPERFICIE_CUBIERTA',
                                                             blank=True, null=True)  # Field name made lowercase.
    clase_afloramiento = models.TextField(db_column='CLASE_AFLORAMIENTO', blank=True,
                                          null=True)  # Field name made lowercase.
    fase_inundacion_encharcamiento = models.TextField(db_column='FASE_INUNDACION_ENCHARCAMIENTO', blank=True,
                                                      null=True)  # Field name made lowercase.
    frecuencia_inundacion = models.TextField(db_column='FRECUENCIA_INUNDACION', blank=True,
                                             null=True)  # Field name made lowercase.
    duracion_inundacion = models.TextField(db_column='DURACION_INUNDACION', blank=True,
                                           null=True)  # Field name made lowercase.
    frecuencia_encharcamiento = models.TextField(db_column='FRECUENCIA_ENCHARCAMIENTO', blank=True,
                                                 null=True)  # Field name made lowercase.
    duracion_encharcamiento = models.TextField(db_column='DURACION_ENCHARCAMIENTO', blank=True,
                                               null=True)  # Field name made lowercase.
    observaciones_horizontes = models.TextField(db_column='OBSERVACIONES_HORIZONTES', blank=True,
                                                null=True)  # Field name made lowercase.
    uso_actual = models.TextField(db_column='USO_ACTUAL', blank=True, null=True)  # Field name made lowercase.
    vegetacion_natural = models.TextField(db_column='VEGETACION_NATURAL', blank=True,
                                          null=True)  # Field name made lowercase.
    nombres_cultivos_pastos = models.TextField(db_column='NOMBRES_CULTIVOS_PASTOS', blank=True,
                                               null=True)  # Field name made lowercase.
    limitante_uso = models.TextField(db_column='LIMITANTE_USO', blank=True, null=True)  # Field name made lowercase.
    clase_clasif_agrologica = models.TextField(db_column='CLASE_CLASIF_AGROLOGICA', blank=True,
                                               null=True)  # Field name made lowercase. This field type is a guess.
    subclase_clasif_agrologica = models.TextField(db_column='SUBCLASE_CLASIF_AGROLOGICA', blank=True,
                                                  null=True)  # Field name made lowercase.
    grietas_ancho_mm = models.TextField(db_column='GRIETAS_ANCHO_mm', blank=True,
                                        null=True)  # Field name made lowercase. This field type is a guess.
    grietas_profundidad_cm = models.TextField(db_column='GRIETAS_PROFUNDIDAD_cm', blank=True,
                                              null=True)  # Field name made lowercase. This field type is a guess.
    caracteristicas_diagnosticas = models.TextField(db_column='CARACTERISTICAS_DIAGNOSTICAS', blank=True,
                                                    null=True)  # Field name made lowercase.
    epipedon = models.TextField(db_column='EPIPEDON', blank=True, null=True)  # Field name made lowercase.
    endopedon_1 = models.TextField(db_column='ENDOPEDON_1', blank=True, null=True)  # Field name made lowercase.
    endopedon_2 = models.TextField(db_column='ENDOPEDON_2', blank=True, null=True)  # Field name made lowercase.
    clasificacion_taxonomica = models.TextField(db_column='CLASIFICACION_TAXONOMICA', blank=True,
                                                null=True)  # Field name made lowercase.
    familia_textural = models.TextField(db_column='FAMILIA_TEXTURAL', blank=True,
                                        null=True)  # Field name made lowercase.
    grados_n = models.TextField(db_column='GRADOS_N', blank=True,
                                null=True)  # Field name made lowercase. This field type is a guess.
    minutos_n = models.TextField(db_column='MINUTOS_N', blank=True,
                                 null=True)  # Field name made lowercase. This field type is a guess.
    segundos_n = models.TextField(db_column='SEGUNDOS_N', blank=True, null=True)  # Field name made lowercase.
    grados_w = models.TextField(db_column='GRADOS_W', blank=True,
                                null=True)  # Field name made lowercase. This field type is a guess.
    minutos_w = models.TextField(db_column='MINUTOS_W', blank=True,
                                 null=True)  # Field name made lowercase. This field type is a guess.
    segundos_w = models.TextField(db_column='SEGUNDOS_W', blank=True, null=True)  # Field name made lowercase.
    latitud = models.TextField(db_column='LATITUD', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    longitud = models.TextField(db_column='LONGITUD', blank=True,
                                null=True)  # Field name made lowercase. This field type is a guess.
    altitud = models.TextField(db_column='ALTITUD', blank=True, null=True)  # Field name made lowercase.
    observaciones_generales = models.TextField(db_column='OBSERVACIONES_GENERALES', blank=True,
                                               null=True)  # Field name made lowercase.
    fase_desp_fam_text = models.TextField(db_column='FASE_desp_fam_text', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bdp_general'


class Coordenadas(models.Model):
    id = models.AutoField(primary_key=True)
    cod_perfil = models.TextField(db_column='COD_PERFIL', blank=True, null=True)  # Field name made lowercase.
    latitud = models.TextField(db_column='LATITUD', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    longitud = models.TextField(db_column='LONGITUD', blank=True,
                                null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'coordenadas'
