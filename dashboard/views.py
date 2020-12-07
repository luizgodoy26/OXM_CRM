from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from clientes.models import Cliente
from contratos.models import Contrato

from django.db.models import Sum


@login_required
def exibeDashboard(request):
    listaClientes = Cliente.objects.all()
    listaContratos = Contrato.objects.all()

    total = Contrato.objects.aggregate(soma=Sum("valorContrato"))
    # Dicionário para passar o valor total dos contratos
    recebimentoTotal = total['soma']

    debitoTotal = Contrato.objects.aggregate(debito=Sum("valorGasto"))
    gastoTotal = debitoTotal['debito']

    profit = recebimentoTotal - gastoTotal


    return render(request, 'dashboard.html', {'listaClientes': listaClientes, 'listaContratos': listaContratos,
                                              'recebimentoTotal': recebimentoTotal, 'gastoTotal': gastoTotal, 'profit': profit})