from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    icono_lucide = models.CharField(
        max_length=50,
        default="folder",
        help_text="Nombre del icono de Lucide (ejemplo: 'folder', 'code', 'user', etc.)"
    )
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    descripcion_corta = models.TextField(max_length=300, help_text="Para la card del Home")
    
    # Cambiado a TextField estándar
    contenido_html = models.TextField('Contenido Detallado HTML')

    habilidades = models.ManyToManyField('Habilidad', related_name='proyectos', blank=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Experiencia(models.Model):
    puesto = models.CharField(max_length=150)
    empresa = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True, help_text="Dejar en blanco si es trabajo actual")
    descripcion = CKEditor5Field('Descripción', config_name='default')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-fecha_inicio', 'orden']

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

class DocumentoCV(models.Model):
    titulo = models.CharField(max_length=100, default="Curriculum Vitae")
    archivo = models.FileField(upload_to='cvs/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_subida']

    def __str__(self):
        return f"CV ({self.fecha_subida:%d/%m/%Y})"

class CVDev(models.Model):
    titulo = models.CharField(max_length=100, default="Curriculum Vitae - Desarrollo")
    archivo = models.FileField(upload_to='cvs/dev/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_subida']

    def __str__(self):
        return f"CV Desarrollo ({self.fecha_subida:%d/%m/%Y})"

class CVUXUI(models.Model):
    titulo = models.CharField(max_length=100, default="Curriculum Vitae - UX/UI")
    archivo = models.FileField(upload_to='cvs/uxui/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_subida']

    def __str__(self):
        return f"CV UX/UI ({self.fecha_subida:%d/%m/%Y})"

class Formacion(models.Model):
    titulo = models.CharField(max_length=150)
    institucion = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True, help_text="Dejar en blanco si es formación en curso")
    descripcion = CKEditor5Field('Descripción', config_name='default')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-fecha_inicio', 'orden']

    def __str__(self):
        return f"{self.titulo} en {self.institucion}"

class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.PositiveIntegerField(help_text="Nivel de habilidad del 1 al 100")
    categoria = models.CharField(max_length=50, choices=[('Desarrollo', 'Desarrollo'), ('Diseño', 'Diseño'), ('Otros', 'Otros')])
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.nombre} ({self.nivel}%)"

class Certificacion(models.Model):
    nombre = models.CharField(max_length=150)
    institucion = models.CharField(max_length=150)
    fecha_obtencion = models.DateField()
    descripcion = CKEditor5Field('Descripción', config_name='default')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-fecha_obtencion', 'orden']

    def __str__(self):
        return f"{self.nombre} en {self.institucion}"

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=150)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.asunto})"




# Create your models here.
