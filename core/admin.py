from django.contrib import admin
from .models import Proyecto, Experiencia, DocumentoCV, MensajeContacto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden')
    ordering = ('orden',)

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('puesto', 'empresa', 'fecha_inicio', 'fecha_fin', 'orden')
    ordering = ('-fecha_inicio', 'orden')

@admin.register(DocumentoCV)
class DocumentoCVAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida')
    ordering = ('-fecha_subida',)

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'fecha_envio')
    ordering = ('-fecha_envio',)
    readonly_fields = ('nombre', 'email', 'asunto', 'mensaje', 'fecha_envio')