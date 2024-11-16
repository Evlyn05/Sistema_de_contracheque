from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, UserModelForm
from django.contrib import messages


def login_(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)

                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            return redirect('login')
    else:
        form = UserModelForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout_(request):
    logout(request)
    return redirect('home')