from django.urls import reverse_lazy

import clientes
from .models import Contrato
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ContratoForm


@login_required
def listaDeContratos(request):
    contratos = Contrato.objects.all()

    return render(request, 'listaDeContratos.html', {'contratos': contratos})


@login_required
def listaDeClientes(request):
    cliente_id = request.GET.get('cliente')
    clientes_nome = clientes.objects.filter(cliente_id=cliente_id).order_by('nome')

    return render(request, 'listaClientes.html', {'clientes_nome': clientes_nome})


@login_required
def criaContrato(request):
    model = Contrato
    fields = ('nome', 'bioContrato', 'cliente', 'valorContrato', 'valorGasto', 'dataContrato', 'dataEntrega', 'arquivos')
    form = ContratoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listaDeContratos')
    return render(request, 'contrato_Form.html', {'form': form})


@login_required
def editaContrato(request, id):
    contrato = get_object_or_404(Contrato, pk=id)
    form_class = ContratoForm
    form = ContratoForm(request.POST or None, request.FILES or None, instance=contrato)


    if form.is_valid():
        form.save()
        return redirect('listaDeContratos')
    return render(request, 'contrato_Form.html', {'form': form})


