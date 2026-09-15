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
    opciones = Habilidad._meta.get_field('categoria').choices
    
    for valor, etiqueta in opciones:
        items = [h for h in todas if h.categoria == valor]
        if items:
            grupos.append({'clave': valor, 'etiqueta': etiqueta, 'items': items})
    return grupos

def curriculum(request):
    ultimo_cv = DocumentoCV.objects.first()
    ultimo_cv_dev = CVDev.objects.first()
    ultimo_cv_uxui = CVUXUI.objects.first()
    
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
        
        # Evaluamos primero si cayó en la trampa del bot (honeypot)
        if form.data.get('website'):
            messages.success(request, "¡Mensaje enviado! Lo revisaré pronto.")
            return redirect('contacto')

        if form.is_valid():
            mensaje_guardado = form.save()
            
            asunto_correo = f"Nuevo contacto: {mensaje_guardado.asunto}"
            cuerpo_correo = f"De: {mensaje_guardado.nombre} ({mensaje_guardado.email})\n\nMensaje:\n{mensaje_guardado.mensaje}"
            
            try:
                send_mail(
                    subject=asunto_correo,
                    message=cuerpo_correo,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['aldo.gonzalez.carquin@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, "¡Mensaje enviado! Lo revisaré pronto.")
                return redirect('contacto')
            except Exception as e:
                print(f"ERROR ENVIANDO CORREO: {e}")
                messages.error(request, "El mensaje se guardó, pero hubo un problema enviando la notificación.")
                return redirect('contacto')
        else:
            messages.error(request, "Revisa los campos del formulario, hay un error.")
    else:
        form = ContactoForm()

    return render(request, 'core/contacto.html', {'form': form})

def detalle_proyecto(request, slug):
    proyecto = get_object_or_404(Proyecto, slug=slug)
    return render(request, 'core/detalle_proyecto.html', {'proyecto': proyecto})
