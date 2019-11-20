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
        encontreiro['data_nascimento'] = request.POST.get('data_nascimento')
        encontreiro['cpf'] = request.POST.get('cpf')
        encontreiro['celular'] = request.POST.get('celular')
        encontreiro['email'] = request.POST.get('email')
        encontreiro['estado_civil'] = request.POST.get('estado_civil')
        encontreiro['cep_encontreiro'] = request.POST.get('cep_encontreiro')
        encontreiro['logradouro_encontreiro'] = request.POST.get('logradouro_encontreiro')
        encontreiro['facebook'] = request.POST.get('facebook')
        encontreiro['numero_encontreiro'] = request.POST.get('numero_encontreiro')
        encontreiro['complemento_encontreiro'] = request.POST.get('complemento_encontreiro')
        encontreiro['bairro_encontreiro'] = request.POST.get('bairro_encontreiro')
        encontreiro['estado_encontreiro'] = request.POST.get('estado_encontreiro')
        encontreiro['cidade_encontreiro'] = request.POST.get('cidade_encontreiro')
        encontreiro['naturalidade_encontreiro'] = request.POST.get('naturalidade_encontreiro')
        encontreiro['email'] = request.POST.get('email')
        encontreiro['frequentando_igreja_enc'] = request.POST.get('frequentando_igreja_enc')
        encontreiro['nome_igreja'] = request.POST.get('nome_igreja')
        encontreiro['local_trabalho_enc'] = request.POST.get('local_trabalho_enc')
        encontreiro['escolaridade_enc'] = request.POST.get('escolaridade_enc')
        encontreiro['curso_encontreiro'] = request.POST.get('curso_encontreiro')
        encontreiro['pessoa_convite_enc'] = request.POST.get('pessoa_convite_enc')
        encontreiro['ano_participacao'] = request.POST.get('ano_participacao')
        encontreiro['equipes_trab'] = request.POST.get('equipes_trab')
        encontreiro['qtd_participacoes'] = request.POST.get('qtd_participacoes')

        Encontreiro.objects.create(**encontreiro)
        success = True
    elif request.method == 'POST':
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
        encontrista['facebook'] = request.POST.get('facebook')
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
        encontrista['local_trabalho'] = request.POST.get('local_trabalho')
        encontrista['nome_escola'] = request.POST.get('nome_escola')
        encontrista['escolaridade'] = request.POST.get('escolaridade')
        encontrista['curso'] = request.POST.get('curso')
        encontrista['pessoas_participando'] = request.POST.get('pessoas_participando')
        encontrista['possui_probsaude'] = request.POST.get('possui_probsaude')
        encontrista['nome_probsaude'] = request.POST.get('nome_probsaude')
        encontrista['telefones_urgencia'] = request.POST.get('telefones_urgencia')
        encontrista['pessoa_convite_enct'] = request.POST.get('pessoa_convite_enct')
        encontrista['telefone_pessoa_convite'] = request.POST.get('telefone_pessoa_convite')
        encontrista['desejo_participacao'] = request.POST.get('desejo_participacao')
        encontrista['pergunta_jesus'] = request.POST.get('pergunta_jesus')

        Encontrista.objects.create(**encontrista)
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'success': success,
    }
    return render(request, 'confirm.html', context)


def login_admin(request):
    return redirect('admin/')
