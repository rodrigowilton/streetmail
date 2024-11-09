from django.urls import path
from . import views

urlpatterns = [
	# Outras URLs
	path('', views.index, name='index'),  # URL raiz mapeada para a view 'index'
	path('entrega/', views.entrega, name='entrega'),  # URL para a entrega
	path('buscar_moradores/<str:apartamento>/', views.buscar_moradores, name='buscar_moradores'),
	# Corrigido para o caminho correto
	path('mail/salvar_correspondencia/', views.salvar_correspondencia, name='salvar_correspondencia'),
	
	path('streetmail', views.streetmail, name='streetmail'),  # URL para o template StreetMail
	path('criar/', views.criar_mail, name='criar_mail'),  # Rota para criar uma nova correspondência/encomenda
	path('confirmacao/', views.confirmacao_mail, name='confirmacao_mail'),  # Rota para a página de confirmação
]
