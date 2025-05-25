from django.contrib import admin
from .models import Estudiante, Docente, Grupo, Area, Calificacion

admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Grupo)
admin.site.register(Area)

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'area', 'periodo', 'nota', 'faltas')
    list_filter  = ('periodo', 'area')

