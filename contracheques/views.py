from django.shortcuts import render, redirect, get_object_or_404
from .models import ContraCheque
from .forms import ContraChequeForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'contracheques/index.html')

@login_required
def listar_contracheques(request):
    contracheques = ContraCheque.objects.all()

    nome = request.GET.get('nome', '')
    ano = request.GET.get('ano', '')

    if nome:
        contracheques = contracheques.filter(nome_funcionario__icontains=nome)

    if ano:
        contracheques = contracheques.filter(ano=ano)

    paginator = Paginator(contracheques, 6)
    page_number = request.GET.get('page')
    contracheques = paginator.get_page(page_number)

    return render(request, 'contracheques/listar-contracheques.html', {'contracheques': contracheques})

@login_required
def criar_contracheque(request):
    if not request.user.is_superuser:
        return redirect('listar-contracheques')

    if request.method == 'POST':
        form = ContraChequeForm(request.POST, request.FILES)
        if form.is_valid():
            contracheque = form.save(commit=False)
            contracheque.usuario = request.user
            contracheque.save()
            return redirect('listar-contracheques')
    else:
        form = ContraChequeForm(initial={'usuario': request.user})

    return render(request, 'contracheques/formulario.html', {'form': form, 'acao': 'cadastrar'})

@login_required
def editar_contracheque(request, id):
    if not request.user.is_superuser:
        return redirect('listar-contracheques')

    contracheque = get_object_or_404(ContraCheque, id=id)
    if request.method == 'POST':
        form = ContraChequeForm(request.POST, request.FILES, instance=contracheque)
        if form.is_valid():
            form.save()
            return redirect('listar-contracheques')
    else:
        form = ContraChequeForm(instance=contracheque)
    
    return render(request, 'contracheques/formulario.html', {'form': form, 'acao': 'editar'})

@login_required
def detalhe_contracheque(request, id):
    contracheque = get_object_or_404(ContraCheque, id=id)    
    return render(request, 'contracheques/detalhe-contracheque.html', {'contracheque': contracheque})

@login_required
def deletar_contracheque(request, id):
    if not request.user.is_superuser:
        return redirect('listar-contracheques')

    contracheque = get_object_or_404(ContraCheque, id=id)
    if request.method == 'POST':
        contracheque.delete()
        return redirect('listar-contracheques')
    
    return render(request, 'contracheques/deletar.html', {'contracheque': contracheque})