from django import forms
from .models import Apto


class AptoForm(forms.ModelForm):
	class Meta:
		model = Apto
		fields = ['morador', 'condominio', 'apto', 'tel', 'email', 'recebeu', 'codigo', 'status']
	
	def clean_email(self):
		# Garante que o email será salvo em minúsculas
		email = self.cleaned_data.get('email')
		return email.lower()  # Converte o email para minúsculas
