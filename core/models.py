from django.db import models
from django.core.mail import send_mail


class Encontreiro(models.Model):
    STATUS_CHOICES = (
        (0, 'Aguardando Pagamento'),
        (1, 'Concluída'),
        (2, 'Cancelada'),
    )

    nome = models.CharField('Nome', max_length=60)
    idade = models.CharField('Idade', max_length=3)
    cpf = models.CharField('CPF', unique=True, max_length=15)
    celular = models.CharField('Celular', max_length=15)
    email = models.EmailField('Email', max_length=50)
    estado_civil = models.CharField('Estado civil', max_length=40)

    cep_encontreiro = models.CharField('CEP', max_length=11)
    logradouro_encontreiro = models.CharField('Logradouro', max_length=40)
    numero_encontreiro = models.CharField('Numero', null=True, max_length=10)
    complemento_encontreiro = models.CharField('Complemento', null=True, blank=True, max_length=60)
    bairro_encontreiro = models.CharField('Bairro', max_length=40)
    estado_encontreiro = models.CharField('Estado', max_length=26)
    cidade_encontreiro = models.CharField('Cidade', max_length=30)

    frequentando_igreja_enc = models.BooleanField('Está frequentando a igreja?')
    nome_igreja = models.CharField('Nome da igreja', null=True, blank=True, max_length=50)

    pessoa_convite_enc = models.CharField('Padrinho ou madrinha', max_length=60)
    ano_participacao = models.IntegerField('Ano de participação')
    equipes_trab = models.CharField('Equipes que já trabalhou', max_length=255)
    qtd_participacoes = models.IntegerField('Quantidade de participações')

    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0
    )
    doenca_cardiaca = models.BooleanField('Possui doença cardíaca?', default=False)
    diabetico = models.BooleanField('É diabético', default=False)
    hipertenso = models.BooleanField('É hipertenso', default=False)
    data_cadastro = models.DateTimeField('Inscrito em', auto_now=True)
    observacoes_gerais = models.TextField('Observações Gerais', null=True)

    def save(self, *args, **kwargs):
        nome = self.nome
        email = self.email
        celular = self.celular
        idade = self.idade
        cpf = self.cpf
        estado_civil = self.estado_civil
        estado_encontreiro = self.estado_encontreiro
        cidade_encontreiro = self.cidade_encontreiro
        nome_igreja = self.nome_igreja
        pessoa_convite_enc = self.pessoa_convite_enc
        ano_participacao = self.ano_participacao
        equipes_trab = self.equipes_trab
        qtd_participacoes = self.qtd_participacoes
        observacoes_gerais = self.observacoes_gerais
        doenca_cardiaca = self.doenca_cardiaca
        diabetico = self.diabetico
        hipertenso = self.hipertenso

        msg = 'Nome: {0}\n'\
              'Celular: {1}\n'\
              'Idade: {2}\n'\
              'CPF: {3}\n'\
              'Estado civil: {4}\n'\
              'Cidade: {5}\n'\
              'Estado: {6}\n'\
              'Igreja: {7}\n'\
              'Padrinho: {8}\n'\
              'Ano que participou: {9}\n'\
              'Equipes que trabalhou: {10}\n'\
              'Quantidade de participações: {11}\n'\
            'Possui alguma doença cardíaca: {12}\n'\
            'É diabético (a): {12}\n'\
            'É hipertenso (a): {13}\n'\
            'Observações gerais: {14}'\
            .format(
                nome, 
                celular, 
                idade, 
                cpf, 
                estado_civil,
                cidade_encontreiro, 
                estado_encontreiro, 
                nome_igreja, 
                pessoa_convite_enc,
                ano_participacao, 
                equipes_trab,
                qtd_participacoes,
                'Sim' if doenca_cardiaca else 'Não',
                'Sim' if diabetico else 'Não',
                'Sim' if hipertenso else 'Não',
                observacoes_gerais
            )
        super(Encontreiro, self).save(*args, **kwargs)
        send_mail(
           subject='INSCRIÇÃO ENCONTREIRO - RJC Santa Inês 2023',
           message='Recebemos seus dados em nosso banco de dados\n' + msg + '\n\nPara concluir a inscrição, por favor efetuar o pagamento!\n'
            'Dados bancários: \n'
            'Chave PIX (email): rjcsantaines2023@gmail.com\n'
            'Favorecido: Elson da Silva Lima\n'
            'Banco: C6 Bank\n\n'
            'Att: Equipe de Direção Geral - RJC 2023',
            from_email='rjcsantaines@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )

    def __str__(self):
        return self.nome


class Encontrista(models.Model):
    STATUS_CHOICES = (
        (0, 'Aguardando Pagamento'),
        (1, 'Concluída'),
        (2, 'Cancelada'),
    )

    TAMANHO_CHOICES = (
        ('P', 'P'),
        ('PP', 'PP'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
    )

    nome_apelido = models.CharField('Nome apelido', null=True, max_length=60)
    data_nascimento_enc = models.DateField('Data de nascimento', null=True, auto_now=False)
    cpf = models.CharField('CPF', unique=True, null=True, max_length=15)
    celular = models.CharField('Celular', null=True, max_length=15)
    estado_civil = models.CharField('Estado civil', null=True, max_length=40)
    email = models.EmailField('Email', null=True, max_length=50)

    cep = models.CharField('CEP', null=True, max_length=10)
    logradouro = models.CharField('Logradouro', null=True, blank=True, max_length=40)
    numero = models.CharField('Numero', null=True, max_length=10)
    complemento = models.CharField('Complemento', null=True, blank=True, max_length=60)
    bairro = models.CharField('Bairro', null=True, blank=True, max_length=25)
    estado = models.CharField('Estado', null=True, max_length=4)
    cidade = models.CharField('Cidade', null=True, max_length=30)
    naturalidade = models.CharField('Naturalidade', null=True, max_length=50)
    
    frequenta_igreja = models.BooleanField('Está frequentando alguma igreja?')
    religiao = models.CharField('Religião', null=True, max_length=30)
    nome_pai = models.CharField('Nome do pai', null=True, blank=True, max_length=100)
    religiao_pai = models.CharField('Religião do pai', null=True, blank=True,  max_length=50)
    nome_mae = models.CharField('Nome da mãe', max_length=100)
    religiao_mae = models.CharField('Religião da mãe', null=True, blank=True, max_length=30)
    
    possui_automovel = models.BooleanField('Possui automóvel?')
    pessoas_moradia = models.CharField('Quem mora na mesma residência', null=True, max_length=70)
    pessoas_participando = models.CharField('Algum conhecido participando do programa?', null=True, max_length=5)
    nome_pessoas_participando = models.CharField('Nome das pessoas', null=True, blank=True, max_length=255)

    alergia = models.BooleanField('Possui algum tipo de alergia?')
    nome_alergia = models.CharField('Qual alergia?', null=True, blank=True, max_length=200)
    diabetico = models.BooleanField('Possui diabetes?')
    hipertenso = models.BooleanField('É hipertenso?')
    cardiaco = models.BooleanField('Tem doença cardíaca?')
    intolerancia = models.BooleanField('Possui intolerância à lactose?')
    remedio_especifico = models.BooleanField('Toma algum remédio específico?')
    nome_remedios = models.CharField('Quais os remédios e horários?', null=True, blank=True, max_length=200)
    problema_saude = models.BooleanField('Tem algum diagnóstico de saúde física ou mental')
    nome_probsaude = models.CharField('Qual diagnóstico de saúde física ou mental?', null=True, blank=True, max_length=200)

    telefones_urgencia = models.CharField('Telefones para urgência', null=True, max_length=40)
    pessoa_convite_enct = models.CharField('Quem o convidou?', null=True, max_length=40)
    telefone_pessoa_convite = models.CharField('Telefone do encontreiro', null=True, max_length=40)
    desejo_participacao = models.TextField('Porque deseja participar do programa?', null=True)
    pergunta_jesus = models.TextField('Quem é Jesus para você?', null=True)
    tamanho_camisa = models.CharField(choices=TAMANHO_CHOICES, max_length=3)
    observacoes_gerais = models.TextField('Observações Gerais', null=True)

    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0, blank=True
    )
    data_cadastro = models.DateTimeField('Inscrito em', null=True, auto_now_add=True)

    def save(self, *args, **kwargs):
        nome_apelido = self.nome_apelido
        data_nascimento_enc = self.data_nascimento_enc
        cpf = self.cpf
        celular = self.celular
        estado_civil = self.estado_civil
        estado = self.estado
        cidade = self.cidade
        email = self.email
        telefones_urgencia = self.telefones_urgencia
        pessoa_convite_enct = self.pessoa_convite_enct
        telefone_pessoa_convite = self.telefone_pessoa_convite
        desejo_participacao = self.desejo_participacao
        pergunta_jesus = self.pergunta_jesus
        observacoes_gerais = self.observacoes_gerais

        msg = 'Nome: {0}\n'\
              'Celular: {1}\nData de nascimento: {2}\n'\
              'CPF: {3}\nEstado civil: {4}\n'\
              'Cidade: {5}\nEstado: {6}\n '\
              'Telefones de emergência: {7}\n'\
                'Quem o convidou: {8}\n'\
              'Telefone de quem o convidou: {9}\n'\
              'Porque deseja participar do programa: {10}\n'\
                'Quem é Jesus para você: {11}\n'\
                'Observações Gerais: {12}\n'\
            .format(nome_apelido, celular, data_nascimento_enc, cpf, estado_civil,
                    cidade, estado, telefones_urgencia, pessoa_convite_enct,
                    telefone_pessoa_convite, desejo_participacao, pergunta_jesus, observacoes_gerais)
        super(Encontrista, self).save(*args, **kwargs)
        send_mail(
            subject='INSCRIÇÃO ENCONTRISTA - RJC Santa Inês 2023',
            message='Recebemos seus dados em nosso banco de dados\n' + msg + '\n\nPara concluir a inscrição, por favor efetuar o pagamento\n'
             'Dados bancários: \n'
            'Chave PIX (email): rjcsantaines2023@gmail.com\n'
            'Favorecido: Elson da Silva Lima\n'
            'Banco: C6 Bank\n\n'
            'Att: Equipe de Direção Geral - RJC 2023',
            from_email='rjcsantaines@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )

    def __str__(self):
        return self.nome_apelido


class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=40, null=False, blank=False, verbose_name='nome_equipe')
    encontreiros = models.ManyToManyField(Encontreiro, related_name='encontreiros',  blank=False)
    qtd_participantes = models.IntegerField(null=True, verbose_name='qtd_participantes')
    nome_coordenador = models.ForeignKey(Encontreiro, related_name='coordenador', on_delete=models.CASCADE, null=True)
    nome_casal_ligacao = models.CharField(max_length=100, null=False, blank=False, verbose_name='nome_casal_ligacao')

    def __str__(self):
        return self.nome_equipe

    def get_encontreiros(self):
        return '\n'.join([str(p) for p in self.encontreiros.all()])


class Circulo(models.Model):
    nome_circulo = models.CharField(max_length=40, null=False, blank=False, verbose_name='nome_circulo')
    encontristas = models.ManyToManyField(Encontrista, blank=False)
    qtd_participantes = models.IntegerField(verbose_name='qtd_participantes')
    lider_circulo = models.ForeignKey(Encontreiro, on_delete=models.SET_NULL, null=True)
    cor_equipe = models.CharField(max_length=20, null=False, blank=False, verbose_name='cor_equipe')

    def __str__(self):
        return self.nome_circulo

    def get_encontristas(self):
        return '\n'.join([str(p) for p in self.encontristas.all()])


class Contato(models.Model):
    nome = models.CharField(max_length=40, verbose_name='Nome')
    email = models.EmailField(max_length=40, verbose_name='Email')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    mensagem = models.TextField(verbose_name='Mensagem')

    def save(self, *args, **kwargs):
        nome = self.nome
        email = self.email
        telefone = self.telefone
        mensagem = self.mensagem
        msg = 'Nome: {0}\nE-mail: {1}\nCelular: {2}\nMensagem: {3}\n'.format(nome, email, telefone, mensagem)
        super(Contato, self).save(*args, **kwargs)
        send_mail(
            'NOVO CONTATO - RJC SANTA INÊS',
            msg,
            'rjcsantaines@gmail.com',
            ['nayanna501@gmail.com'],
            fail_silently=False,
        )

    def __str__(self):
        return self.nome