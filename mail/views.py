from django.db.models.fields import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    # Filtra os moradores pelo campo "apto"
    moradores = Apto.objects.filter(apto=apartamento)  # Ajuste conforme o nome correto do campo
    moradores_data = [{"id": morador.id, "morador": morador.morador} for morador in moradores]
    return JsonResponse({"moradores": moradores_data})

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
		tipo = int(request.POST.get('tipo'))  # Convertendo para inteiro
		comando = request.POST.get('comando')
		
		# Gerar um código único
		codigo = gerar_codigo()
		
		# Verificar qual gaveta está disponível, se o tipo de encomenda for 'Encomenda Pequena'
		gaveta_aberta = None
		
		if tipo == Mail.ENCOMENDAPEQUENA:
			# Procurar gavetas pequenas disponíveis
			for i in range(1, 7):  # Existem 6 gavetas pequenas
				gaveta_field = f'gaveta_pequena{i}'
				gaveta = getattr(Mail.objects.first(), gaveta_field)  # Acessa a gaveta para verificar o status
				
				if not gaveta:  # Se a gaveta estiver disponível (False)
					# Atualiza a gaveta como ocupada (True)
					mail = Mail.objects.first()
					setattr(mail, gaveta_field, True)
					mail.save()  # Salva as alterações no banco
					gaveta_aberta = f'Gaveta Pequena {i}'  # Armazenar a gaveta aberta
					break
		
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
		if gaveta_aberta:
			messages.success(request,
							 f'Encomenda criada com sucesso! Código: {codigo}. A encomenda foi alocada na {gaveta_aberta}.')
		else:
			messages.success(request,
							 f'Encomenda criada com sucesso! Código: {codigo}. Não foi possível alocar a encomenda em uma gaveta disponível.')
		
		return redirect('confirmacao_mail')  # Redireciona para uma página de confirmação
	
	return render(request, 'criar_mail.html')

# View para mostrar a página de confirmação

@csrf_exempt
def salvar_correspondencia(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		apartamento = data.get('apartamento')
		morador = data.get('morador')
		tipo = data.get('tipo')
		codigo = data.get('codigo')
		
		# Salve a correspondência no banco de dados, por exemplo:
		Mail.objects.create(
			apartamento=apartamento,
			morador=morador,
			tipo=tipo,
			codigo=codigo,
		)
		
		return JsonResponse({'success': True, 'message': 'Correspondência salva com sucesso!'})
	
	return JsonResponse({'success': False, 'message': 'Método inválido.'}, status=400)


def confirmacao_mail(request):
	return render(request, 'confirmacao_mail.html')
