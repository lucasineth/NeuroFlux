from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pacientes
from django.contrib import messages
from django.contrib.messages import constants

def pacientes(request):
    if request.method == 'GET':
        pacientes = Pacientes.objects.all()
        queixas = Pacientes.queixa_choice
        return render(request, 'pacientes.html', {'queixas': queixas, 'pacientes': pacientes})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request, constants.ERROR, 'Por favor, preencha todos os campos obrigatórios.')
            return redirect('pacientes')
        
        paciente = Pacientes(nome=nome, email=email, telefone=telefone, queixa=queixa, foto=foto)
        paciente.save()
        messages.add_message(request, constants.SUCCESS, 'Paciente cadastrado com sucesso.')
        return redirect('pacientes')

def paciente_view(request, id):
    paciente = Pacientes.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'paciente_view.html', {'paciente': paciente})    