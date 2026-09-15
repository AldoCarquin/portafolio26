from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    # --- EL CAMPO HONEYPOT (Trampa para bots) ---
    website = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'hp-field', 'autocomplete': 'off', 'tabindex': '-1'})
    )

    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@correo.com'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '¿De qué trata?'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cuéntame tu proyecto...'}),
        }

    def clean_website(self):
        val = self.cleaned_data.get('website')
        if val:
            raise forms.ValidationError("Spam detectado.")
        return val
        return val
