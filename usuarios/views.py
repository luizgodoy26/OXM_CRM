from django.shortcuts import render, redirect


# Create your views here.
from usuarios.forms import CriaUsuarioForm


def criaUsuarioView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CriaUsuarioForm()
        if request.method == 'POST':
            form = CriaUsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                CriaUsuarioForm.success(request, 'Conta criada: ' + user)

                return redirect('login')

        return render(request, 'registrar.html', {'form': form})