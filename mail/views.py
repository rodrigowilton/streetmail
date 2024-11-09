from django.shortcuts import render, redirect
from django.http import JsonResponse
from app.models import Mail, Apto
from django.contrib import messages
import random
import string


# Função para gerar um código aleatório
def gerar_codigo():
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


def index(request):
	# Buscando o nome do condomínio do primeiro apartamento (ou todos se preferir)
	apto = Apto.objects.first()  # Ou use .all() para todos os apartamentos
	condominio = apto.condominio if apto else "Nome do Condomínio não encontrado"  # Caso não encontre nenhum
	
	return render(request, 'index.html', {'condominio': condominio})


def entrega(request):
	primeiro = Apto.objects.first()
	condominio = primeiro.condominio
	moradores = []
	
	if request.method == "POST":
		apartamento = request.POST.get('apartamento')
		moradores = Apto.objects.filter(apto=apartamento,
										status=True)  # Filtra moradores ativos no apartamento informado
	
	return render(request, 'streetmail.html', {'condominio': condominio, 'moradores': moradores})


def buscar_moradores(request, apartamento):
	moradores = Apto.objects.filter(apto=apartamento, status=True)  # Filtra moradores ativos
	moradores_list = [{"id": morador.id, "morador": morador.morador} for morador in moradores]
	return JsonResponse({"moradores": moradores_list})


def streetmail(request):
	# Exemplos de dados para passar para o template
	condominio = "Condomínio Exemplo"
	codigo = "ABCD1234"
	
	# Você pode preencher a lista de moradores de forma dinâmica
	moradores = [
		{'id': 1, 'nome': 'Morador 1'},
		{'id': 2, 'nome': 'Morador 2'},
	]
	
	return render(request, 'streetmail.html', {
		'condominio': condominio,
		'codigo': codigo,
		'moradores': moradores
	})


# View para criar uma nova correspondência/encomenda
def criar_mail(request):
	if request.method == 'POST':
		morador = request.POST.get('morador')
		condominio = request.POST.get('condominio')
		apto = request.POST.get('apto')
		tel = request.POST.get('tel')
		email = request.POST.get('email')
		tipo = request.POST.get('tipo')
		comando = request.POST.get('comando')
		
		# Gerar um código único
		codigo = gerar_codigo()
		
		# Criar o objeto Mail
		mail = Mail(
			morador=morador,
			condominio=condominio,
			apto=apto,
			tel=tel,
			email=email,
			tipo=tipo,
			comando=comando,
			codigo=codigo
		)
		mail.save()
		
		# Exibir mensagem de sucesso
		messages.success(request, f'Correspondência/Encomenda criada com sucesso! Código: {codigo}')
		return redirect('confirmacao_mail')  # Redireciona para uma página de confirmação
	
	return render(request, 'criar_mail.html')


# View para mostrar a página de confirmação
def confirmacao_mail(request):
	return render(request, 'confirmacao_mail.html')
