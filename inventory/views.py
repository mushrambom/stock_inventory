from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def display_bonecas(request):
    items = Bonecas.objects.all()
    context = {
        'items' : items,
        'header' : 'Bonecas',
    }
    return render(request, 'index.html', context)

def display_bonecos(request):
    items = Bonecos.objects.all()
    context = {
        'items' : items,
        'header' : 'Bonecos',
    }
    return render(request, 'index.html', context)

def display_outros(request):
    items = Outros.objects.all()
    context = {
        'items' : items,
        'header' : 'Outros',
    }
    return render(request, 'index.html', context)

def display_brindes(request):
    items = Brindes.objects.all()
    context = {
        'items' : items,
        'header' : 'Brindes',
    }
    return render(request, 'index.html', context)

def display_carros(request):
    items = Carros.objects.all()
    context = {
        'items' : items,
        'header' : 'Carros',
    }
    return render(request, 'index.html', context)

def display_jogos(request):
    items = Jogos.objects.all()
    context = {
        'items' : items,
        'header' : 'Jogos',
    }
    return render(request, 'index.html', context)

def add_toy(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', { 'form' : form })

def add_boneca(request):
    return add_toy(request, BonecasForm)

def add_boneco(request):
    return add_toy(request, BonecosForm)

def add_carro(request):
    return add_toy(request, CarrosForm)

def add_jogo(request):
    return add_toy(request, JogosForm)

def add_brinde(request):
    return add_toy(request, BrindesForm)

def add_outro(request):
    return add_toy(request, OutrosForm)

def edit_toy(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form' : form})

def edit_boneca(request, pk):
    return edit_toy(request, pk, Bonecas, BonecasForm)