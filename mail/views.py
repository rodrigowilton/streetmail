from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from app.models import Mail
from django.contrib import messages
import random
import string

# Função para gerar um código aleatório
def gerar_codigo():
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def index(request):
    return render(request, 'index.html')


def entrega(request):
    # Aqui você pode passar o contexto necessário, como o nome do condomínio
    condominio = "Nome do Condomínio"  # Altere conforme a necessidade
    return render(request, 'streetmail.html', {'condominio': condominio})
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
        codigo = generate_codigo()

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
