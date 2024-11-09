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

    return render(request, "criar_apto.html", {"form": form})


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
    return render(request, "listar_aptos.html", {"aptos": aptos})
