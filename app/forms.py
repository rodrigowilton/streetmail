from django import forms
from .models import Apto

class AptoForm(forms.ModelForm):
    class Meta:
        model = Apto
        fields = ['morador', 'condominio', 'apto', 'tel', 'email', 'recebeu', 'codigo', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define o primeiro condomínio como valor padrão
        self.fields['condominio'].initial = Apto.objects.first().condominio if Apto.objects.first() else None
        self.fields['condominio'].widget.attrs['readonly'] = 'readonly'

    def clean_email(self):
        # Garante que o email será salvo em minúsculas
        email = self.cleaned_data.get('email')
        return email.lower()  # Converte o email para minúsculas
