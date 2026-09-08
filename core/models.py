from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    url_sitio = models.URLField(blank=True, null=True)
    url_repo = models.URLField(blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.titulo

class Experiencia(models.Model):
    puesto = models.CharField(max_length=150)
    empresa = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True, help_text="Dejar en blanco si es trabajo actual")
    descripcion = models.TextField()
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
        return f"{self.titulo} - {self.fecha_subida.strftime('%Y-%m-%d')}"

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=150)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.asunto})"

# Create your models here.
