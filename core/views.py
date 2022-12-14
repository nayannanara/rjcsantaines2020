from django.shortcuts import render, redirect
from .models import Contato, Encontreiro, Encontrista
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def contato(request):
    success = False
    if request.method == 'POST':
        contato = {}
        contato['nome'] = request.POST.get('nome')
        contato['telefone'] = request.POST.get('telefone')
        contato['email'] = request.POST.get('email')
        contato['mensagem'] = request.POST.get('mensagem')

        Contato.objects.create(**contato)
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'success': success
    }
    return render(request, '_contato.html', context)


def encontreiro_novo(request):
    success = False
    if request.method == 'POST':
        encontreiro = {}
        encontreiro['nome'] = request.POST.get('nome')
        encontreiro['idade'] = request.POST.get('idade')
        encontreiro['cpf'] = request.POST.get('cpf')
        encontreiro['celular'] = request.POST.get('celular')
        encontreiro['email'] = request.POST.get('email')
        encontreiro['estado_civil'] = request.POST.get('estado_civil')
        encontreiro['cep_encontreiro'] = request.POST.get('cep_encontreiro')
        encontreiro['logradouro_encontreiro'] = request.POST.get('logradouro_encontreiro')
        encontreiro['numero_encontreiro'] = request.POST.get('numero_encontreiro')
        encontreiro['complemento_encontreiro'] = request.POST.get('complemento_encontreiro')
        encontreiro['bairro_encontreiro'] = request.POST.get('bairro_encontreiro')
        encontreiro['estado_encontreiro'] = request.POST.get('estado_encontreiro')
        encontreiro['cidade_encontreiro'] = request.POST.get('cidade_encontreiro')
        encontreiro['email'] = request.POST.get('email')
        encontreiro['frequentando_igreja_enc'] = request.POST.get('frequentando_igreja_enc')
        encontreiro['nome_igreja'] = request.POST.get('nome_igreja')
        encontreiro['pessoa_convite_enc'] = request.POST.get('pessoa_convite_enc')
        encontreiro['ano_participacao'] = request.POST.get('ano_participacao')
        encontreiro['equipe_participar'] = request.POST.get('equipe_participar')
        encontreiro['qtd_participacoes'] = request.POST.get('qtd_participacoes')
        encontreiro['doenca_cardiaca'] = request.POST.get('doenca_cardiaca')
        encontreiro['diabetico'] = request.POST.get('diabetico')
        encontreiro['hipertenso'] = request.POST.get('hipertenso')
        encontreiro['observacoes_gerais'] = request.POST.get('observacoes_gerais')

        Encontreiro.objects.create(**encontreiro)
        success = True
    elif request.method == 'GET':
        messages.error(request, 'Formulário inválido')
    context = {
        'success': success
    }
    return render(request, 'confirm.html', context)


def encontrista_novo(request):
    success = False
    if request.method == 'POST':
        encontrista = {}
        encontrista['nome_apelido'] = request.POST.get('nome_apelido')
        encontrista['data_nascimento_enc'] = request.POST.get('data_nascimento_enc')
        encontrista['cpf'] = request.POST.get('cpf')
        encontrista['celular'] = request.POST.get('celular')
        encontrista['email'] = request.POST.get('email')
        encontrista['estado_civil'] = request.POST.get('estado_civil')
        encontrista['cep'] = request.POST.get('cep')
        encontrista['logradouro'] = request.POST.get('logradouro')
        encontrista['numero'] = request.POST.get('numero')
        encontrista['complemento'] = request.POST.get('complemento')
        encontrista['bairro'] = request.POST.get('bairro')
        encontrista['estado'] = request.POST.get('estado')
        encontrista['cidade'] = request.POST.get('cidade')
        encontrista['naturalidade'] = request.POST.get('naturalidade')
        encontrista['email'] = request.POST.get('email')
        encontrista['frequenta_igreja'] = request.POST.get('frequenta_igreja')
        encontrista['religiao'] = request.POST.get('religiao')
        encontrista['nome_pai'] = request.POST.get('nome_pai')
        encontrista['religiao_pai'] = request.POST.get('religiao_pai')
        encontrista['nome_mae'] = request.POST.get('nome_mae')
        encontrista['religiao_mae'] = request.POST.get('religiao_mae')
        encontrista['possui_automovel'] = request.POST.get('possui_automovel')
        encontrista['pessoas_moradia'] = request.POST.get('pessoas_moradia')
        encontrista['pessoas_participando'] = request.POST.get('pessoas_participando')
        encontrista['problema_saude'] = request.POST.get('problema_saude')
        encontrista['nome_probsaude'] = request.POST.get('nome_probsaude')
        encontrista['telefones_urgencia'] = request.POST.get('telefones_urgencia')
        encontrista['pessoa_convite_enct'] = request.POST.get('pessoa_convite_enct')
        encontrista['telefone_pessoa_convite'] = request.POST.get('telefone_pessoa_convite')
        encontrista['desejo_participacao'] = request.POST.get('desejo_participacao')
        encontrista['pergunta_jesus'] = request.POST.get('pergunta_jesus')
        encontrista['alergia'] = request.POST.get('alergia')
        encontrista['nome_alergia'] = request.POST.get('nome_alergia')
        encontrista['diabetico'] = request.POST.get('diabetico')
        encontrista['hipertenso'] = request.POST.get('hipertenso')
        encontrista['cardiaco'] = request.POST.get('cardiaco')
        encontrista['intolerancia'] = request.POST.get('intolerancia')
        encontrista['remedio_especifico'] = request.POST.get('remedio_especifico')
        encontrista['nome_remedios'] = request.POST.get('nome_remedios')
        encontrista['tamanho_camisa'] = request.POST.get('tamanho_camisa')
        encontrista['observacoes_gerais'] = request.POST.get('observacoes_gerais')
        encontrista['nome_pessoas_participando'] = request.POST.get('nome_pessoas_participando')

        Encontrista.objects.create(**encontrista)
        success = True
    elif request.method == 'GET':
        messages.error(request, 'Formulário inválido')
    context = {
        'success': success,
    }
    return render(request, 'confirm.html', context)


def login_admin(request):
    return redirect('admin/')
