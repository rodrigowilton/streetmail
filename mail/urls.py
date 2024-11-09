from django.urls import path
from . import views

urlpatterns = [
    # Outras URLs
    path('', views.index, name='index'),  # URL raiz mapeada para a view 'index'
    path('entrega/', views.entrega, name='entrega'),  # URL para a entrega
    
    path('streetmail', views.streetmail, name='streetmail'),  # URL para o template StreetMail
    # Rota para criar uma nova correspondência/encomenda
    path('criar/', views.criar_mail, name='criar_mail'),

    # Rota para a página de confirmação após a criação
    path('confirmacao/', views.confirmacao_mail, name='confirmacao_mail'),

]
