from django import forms
from django.contrib import admin
from django_ace import AceWidget
from .models import (
    Proyecto, Experiencia, DocumentoCV, MensajeContacto, 
    CVDev, CVUXUI, Formacion, Habilidad, Certificacion
)

class ProyectoAdminForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'contenido_html': AceWidget(
                mode='html',
                theme='monokai',
                width='100%',
                height='600px',
                toolbar=True,
                fontsize='14px'
            ),
        }

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    form = ProyectoAdminForm
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

@admin.register(CVDev)
class CVDevAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida')
    ordering = ('-fecha_subida',)  

@admin.register(CVUXUI)
class CVUXUIAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida')
    ordering = ('-fecha_subida',)

@admin.register(Formacion)
class FormacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'fecha_inicio', 'fecha_fin', 'orden')
    ordering = ('-fecha_inicio', 'orden')

@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    ordering = ('nombre',)

@admin.register(Certificacion)
class CertificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'institucion', 'fecha_obtencion', 'orden')
    ordering = ('-fecha_obtencion', 'orden')