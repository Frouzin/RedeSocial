# core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Postagem, Comentario, Perfil

@login_required
def feed(request):
    postagens = Postagem.objects.all().order_by('-data_criacao')
    return render(request, 'core/feed.html', {'postagens': postagens})

@login_required
def perfil(request, username):
    user = get_object_or_404(User, username=username)
    perfil = get_object_or_404(Perfil, user=user)
    postagens = Postagem.objects.filter(autor=user).order_by('-data_criacao')
    return render(request, 'core/perfil.html', {'perfil': perfil, 'postagens': postagens})

def index(request):
    postagens = Postagem.objects.all()
    return render(request, 'core/index.html', {'postagens': postagens})

def post_detail(request, id):
    postagem = get_object_or_404(Postagem, id=id)
    return render(request, 'core/post_detail.html', {'postagem': postagem})

def perfil_detail(request, id):
    perfil = get_object_or_404(Perfil, id=id)
    return render(request, 'core/perfil_detail.html', {'perfil': perfil})
