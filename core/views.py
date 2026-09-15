from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Proyecto, Experiencia, DocumentoCV, CVDev, CVUXUI, Formacion, Habilidad, Certificacion
from .forms import ContactoForm
from django.conf import settings

def home(request):
    proyectos = Proyecto.objects.all()
    experiencias = Experiencia.objects.all()
    ultimo_cv = DocumentoCV.objects.first()

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.')
            return redirect('home')
    else:
        form = ContactoForm()

    context = {
        'proyectos': proyectos,
        'experiencias': experiencias,
        'ultimo_cv': ultimo_cv,
        'form': form,
    }

    return render(request, 'core/index.html', context)

def agrupar_habilidades():
    todas = Habilidad.objects.all().order_by('orden')
    grupos = []
    # Accede directamente a las opciones del campo 'categoria'
    opciones = Habilidad._meta.get_field('categoria').choices
    
    for valor, etiqueta in opciones:
        items = [h for h in todas if h.categoria == valor]
        if items:
            grupos.append({'clave': valor, 'etiqueta': etiqueta, 'items': items})
    return grupos

def curriculum(request):
    ultimo_cv = DocumentoCV.objects.first()
    ultimo_cv_dev = CVDev.objects.first()      # Consulta directa a CVDev
    ultimo_cv_uxui = CVUXUI.objects.first()    # Consulta directa a CVUXUI
    
    experiencias = Experiencia.objects.all()
    formaciones = Formacion.objects.all()
    habilidades = Habilidad.objects.all()
    certificaciones = Certificacion.objects.all()
    
    context = {
        'ultimo_cv': ultimo_cv,
        'ultimo_cv_dev': ultimo_cv_dev,
        'ultimo_cv_uxui': ultimo_cv_uxui,
        'experiencias': experiencias,
        'formaciones': formaciones,
        'habilidades_grupos': agrupar_habilidades(),
        'certificaciones': certificaciones,
    }
    return render(request, 'core/curriculum.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        
        if form.is_valid():
            # 1. Guardamos el mensaje en la base de datos de Django
            mensaje_guardado = form.save()
            
            # 2. Preparamos y enviamos el correo a tu bandeja personal
            asunto_correo = f"Nuevo contacto: {mensaje_guardado.asunto}"
            cuerpo_correo = f"De: {mensaje_guardado.nombre} ({mensaje_guardado.email})\n\nMensaje:\n{mensaje_guardado.mensaje}"
            
            try:
                send_mail(
                    subject=asunto_correo,
                    message=cuerpo_correo,
                    from_email=settings.DEFAULT_FROM_EMAIL, # Sigue saliendo desde tu cuenta cartero
                    recipient_list=['aldo.gonzalez.carquin@gmail.com'], # ¡Aquí llega directo a ti!
                    fail_silently=False,
                )
                messages.success(request, "¡Mensaje enviado! Lo revisaré pronto.")
                return redirect('contacto')
            except Exception as e:
                # Si el correo falla, igual quedó guardado en la base de datos
                messages.error(request, "El mensaje se guardó, pero hubo un problema enviando la notificación.")
                
        else:
            # Si el bot cayó en la trampa (el campo website tiene texto)
            if 'website' in form.errors:
                # Le hacemos creer al bot que tuvo éxito para que no intente saltar la barrera
                messages.success(request, "¡Mensaje enviado! Lo revisaré pronto.")
                return redirect('contacto')
            else:
                messages.error(request, "Revisa los campos del formulario, hay un error.")
    else:
        form = ContactoForm()

    return render(request, 'core/contacto.html', {'form': form})

def detalle_proyecto(request, slug):
    proyecto = get_object_or_404(Proyecto, slug=slug)
    return render(request, 'core/detalle_proyecto.html', {'proyecto': proyecto})