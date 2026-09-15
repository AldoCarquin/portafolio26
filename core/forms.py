from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    # --- EL CAMPO HONEYPOT (Trampa para bots) ---
    # Este campo NO está en tu base de datos, solo vive en este formulario
    website = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'hp-field', 'autocomplete': 'off'})
    )

    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        
        # Aquí le damos las clases CSS y placeholders a tus campos reales
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@correo.com'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '¿De qué trata?'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cuéntame tu proyecto...'}),
        }

    def clean_website(self):
        # Si un bot llena este campo, lo bloqueamos
        val = self.cleaned_data.get('website')
        if val:
            raise forms.ValidationError("Spam detectado.")
        return val
