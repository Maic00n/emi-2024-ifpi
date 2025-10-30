from django.shortcuts import render

def index(request):
    return render(request, 'aluno/index.html')

def cadastro(request):
    return render(request, 'aluno/cadastro.html')