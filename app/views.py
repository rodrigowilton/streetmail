from django.shortcuts import render, redirect, get_object_or_404
from app.models import Apto, Mail
from .forms import AptoForm
def criar_apto(request):
    if request.method == "POST":
        form = AptoForm(request.POST)
        if form.is_valid():
            # Salva o apartamento
            apartamento = form.save()

            # Criando o Mail relacionado ao Apto criado
            mail = Mail(
                morador=apartamento.morador,
                condominio=apartamento.condominio,
                apto=apartamento.apto,
                tel=apartamento.tel,
                email=apartamento.email,
                recebeu=apartamento.recebeu,  # Utiliza o mesmo valor de 'recebeu' do Apto
                codigo=apartamento.codigo,  # Utiliza o mesmo código do Apto
                tipo=Mail.CORRESPONDENCIA,  # Pode ser alterado para ENCOMENDA se necessário
                status=apartamento.status,  # Utiliza o mesmo status do Apto
                comando=1  # Ajuste conforme o valor desejado para o comando
            )
            mail.save()  # Salva o modelo Mail

            return redirect("listar_aptos")  # Redireciona para a listagem de apartamentos

    else:
        form = AptoForm()

        # Verifica se existem condomínios no banco
        if not Apto.objects.exists():  # Se não existir nenhum apartamento (e, por consequência, condomínio)
            # Torna o campo condominio editável
            form.fields['condominio'].widget.attrs.pop('readonly', None)

    return render(request, "criar_apto.html", {"form": form})

def cadicionar_morador(request):
    if request.method == "POST":
        form = AptoForm(request.POST)
        if form.is_valid():
            # Atribuindo o primeiro condomínio como valor padrão
            condominio = Apto.objects.first()  # Busca o primeiro condomínio da tabela

            # Obtendo os dados do formulário
            apartamento = form.save(commit=False)  # Não salva ainda, para modificar o campo 'condominio'

            # Define o condomínio no apartamento
            if condominio:
                apartamento.condominio = condominio

            apartamento.save()  # Agora salva o apartamento com o condomínio atribuído

            # Criando o Mail relacionado ao Apto criado
            mail = Mail(
                morador=apartamento.morador,
                condominio=apartamento.condominio,
                apto=apartamento.apto,
                tel=apartamento.tel,
                email=apartamento.email,
                recebeu=apartamento.recebeu,  # Utiliza o mesmo valor de 'recebeu' do Apto
                codigo=apartamento.codigo,  # Utiliza o mesmo código do Apto
                tipo=Mail.CORRESPONDENCIA,  # Pode ser alterado para ENCOMENDA se necessário
                status=apartamento.status,  # Utiliza o mesmo status do Apto
                comando=1  # Ajuste conforme o valor desejado para o comando
            )
            mail.save()  # Salva o modelo Mail

            return redirect("listar_aptos")  # Redireciona para a listagem de apartamentos

    else:
        form = AptoForm()

    return render(request, "adicionar_morador.html", {"form": form})

def editar_apto(request, pk):
    apto = get_object_or_404(Apto, pk=pk)
    if request.method == "POST":
        form = AptoForm(request.POST, instance=apto)
        if form.is_valid():
            form.save()
            return redirect("listar_aptos")
    else:
        form = AptoForm(instance=apto)
    return render(request, "editar_apto.html", {"form": form, "apto": apto})

def deletar_apto(request, pk):
    apto = get_object_or_404(Apto, pk=pk)
    if request.method == "POST":
        # Alterando o status para 0 (inativo)
        apto.status = 0
        apto.save()
        return redirect("listar_aptos")
    return render(request, "deletar_apto.html", {"apto": apto})

def listar_aptos(request):
    aptos = Apto.objects.all()

    # Verifica se existe pelo menos um apartamento (condomínio)
    existe_condominio = aptos.exists()

    # Verifica se existe pelo menos um morador (campo morador não nulo)
    existe_morador = aptos.filter(morador__isnull=False).exists()

    return render(request, 'listar_aptos.html', {
        'aptos': aptos,
        'existe_condominio': existe_condominio,
        'existe_morador': existe_morador
    })
