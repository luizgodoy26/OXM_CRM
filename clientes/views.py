from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Pessoa
from .forms import ClienteForm


# Exibe os clientes cadastrados
def listaDeCleintes(request):
    # O manager objects permite que sejam procurados objetos de diversas formas
    # A função all() retorna todos os objetos da classe cleinte
    clientes = Cliente.objects.all()

    return render(request, 'cliente.html', {'clientes': clientes})


#Cria um cadastro de cliente
def criaCliente(request):
    # Se a pessoa clicar em enviar já tendo os dados preenchidos, aciona o POST
    # Se não, envia um post vazio (None)
    # O request.FILES serve para que arquivos de mídia também sejam enviados
    form = ClienteForm(request.POST or None, request.FILES or None)

    # Valida se o formulário é valido
    if form.is_valid():
        form.save()
        # Redireciona à lista de clientes
        return redirect('listaCliente')
        # Envia o formulário já através do form se já estiver preenchido
    return render(request, 'cliente_formulario.html', {'form': form})


# Edita o cliente com o ID equivalente
def editaCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form_class = ClienteForm
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('listaClie  nte')
    return render(request, 'cliente_formulario.html', {'form': form_class})


# Delta o cliente com ID equivalente
def deletaCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form_class = ClienteForm
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    # Verifica se já está tudo ok para deleção
    if request.method == 'POST':
        cliente.delete()
        return redirect('listaCliente')

    else:
        return render(request, 'confima_delecao_cliente.html', {'cliente': cliente})

