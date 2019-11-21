from django.db import models
from django.core.mail import send_mail


class Encontreiro(models.Model):
    nome = models.CharField('Nome', null=True, max_length=60)
    data_nascimento = models.DateField('Data de nascimento', null=True, auto_now=False)
    cpf = models.CharField('CPF', unique=True, null=True, max_length=15)
    celular = models.CharField('Celular',  null=True, max_length=15)
    email = models.EmailField('Email',  null=True, max_length=50)
    estado_civil = models.CharField('Estado civil',  null=True, max_length=40)
    facebook = models.CharField('Facebook', null=True, blank=True, max_length=50)
    cep_encontreiro = models.CharField('CEP', null=True, max_length=11)
    naturalidade_encontreiro = models.CharField('Naturalidade', null=True, max_length=50)
    logradouro_encontreiro = models.CharField('Logradouro', null=True, blank=True, max_length=40)
    numero_encontreiro = models.IntegerField('Numero', null=True)
    complemento_encontreiro = models.CharField('Complemento', null=True, blank=True, max_length=60)
    bairro_encontreiro = models.CharField('Bairro', null=True, blank=True, max_length=40)
    estado_encontreiro = models.CharField('Estado', null=True, max_length=26)
    cidade_encontreiro = models.CharField('Cidade', null=True, max_length=30)
    frequentando_igreja_enc = models.CharField('Está frequentando a igreja?', null=True, max_length=5)
    nome_igreja = models.CharField('Nome da igreja', null=True, max_length=50)
    local_trabalho_enc = models.CharField('Local de trabalho', null=True, blank=True, max_length=40)
    escolaridade_enc = models.CharField('Escolaridade', null=True, blank=True, max_length=40)
    pessoa_convite_enc = models.CharField('Padrinho ou madrinha', null=True, max_length=30)
    ano_participacao = models.IntegerField('Ano de participação', null=True)
    equipes_trab = models.CharField('Equipes que já trabalhou', null=True, max_length=70)
    curso_encontreiro = models.CharField('Curso', max_length=70, null=True, blank=True)
    qtd_participacoes = models.IntegerField('Quantidade de participações', null=True)

    STATUS_CHOICES = (
        (0, 'Aguardando Pagamento'),
        (1, 'Concluída'),
        (2, 'Cancelada'),
    )
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0, blank=True
    )
    data_cadastro = models.DateTimeField('Inscrito em', null=True, auto_now_add=True)

    def save(self, *args, **kwargs):
        nome = self.nome
        email = self.email
        celular = self.celular
        data_nascimento = self.data_nascimento
        cpf = self.cpf
        estado_civil = self.estado_civil
        facebook = self.facebook
        estado_encontreiro = self.estado_encontreiro
        cidade_encontreiro = self.cidade_encontreiro
        nome_igreja = self.nome_igreja
        pessoa_convite_enc = self.pessoa_convite_enc
        ano_participacao = self.ano_participacao
        equipes_trab = self.equipes_trab
        qtd_participacoes = self.qtd_participacoes
        msg = 'Nome: {0}\n'\
              'Celular: {1}\n'\
              'Data de nascimento: {2}\n'\
              'CPF: {3}\n'\
              'Estado civil: {4}\n'\
              'Facebook: {5}\n'\
              'Cidade: {6}\n'\
              'Estado: {7}\n'\
              'Igreja: {8}\n'\
              'Padrinho: {9}\n'\
              'Ano que participou: {10}\n'\
              'Equipes que trabalhou: {11}\n'\
              'Quantidade de participações: {12}\n'\
            .format(nome, celular, data_nascimento, cpf, estado_civil, facebook,
                    cidade_encontreiro, estado_encontreiro, nome_igreja, pessoa_convite_enc,
                    ano_participacao, equipes_trab, qtd_participacoes)
        super(Encontreiro, self).save(*args, **kwargs)
        send_mail(
            'INSCRIÇÃO ENCONTREIRO - RJC 2020',
            'Recebemos seus dados em nosso banco de dados\n' + msg + '\n\nPara concluir a inscrição, por favor efetuar o pagamento\n'
            'Dados bancários: \n'
            'Agência: 0768\nTipo de conta: 013\nConta: 00045215-5\n'
            'Banco Caixa Econômica Federal\n'
            'Favorecida: Jessica Aline Souza Lima\n'
            'Informações importantes: Não serão aceitos depósitos em envelopes, sob pena de não ser reconhecida a inscrição\n'
            'Depósitos apenas de forma direta "boca do caixa", lotéricas e/ou transferências bancárias\n\n\n'
            'Att: Equipe de direção geral - RJC 2020',
            'rjcsantaines@gmail.com',
            [email],
            fail_silently=False,
        )

    def __str__(self):
        return self.nome


class Encontrista(models.Model):
    nome_apelido = models.CharField('Nome apelido', null=True, max_length=60)
    data_nascimento_enc = models.DateField('Data de nascimento', null=True, auto_now=False)
    cpf = models.CharField('CPF', unique=True, null=True, max_length=15)
    celular = models.CharField('Celular', null=True, max_length=15)
    estado_civil = models.CharField('Estado civil', null=True, max_length=40)
    cep = models.CharField('CEP', null=True, max_length=10)
    logradouro = models.CharField('Logradouro', null=True, blank=True, max_length=40)
    numero = models.IntegerField('Numero', null=True)
    complemento = models.CharField('Complemento', null=True, blank=True, max_length=60)
    bairro = models.CharField('Bairro', null=True, blank=True, max_length=25)
    estado = models.CharField('Estado', null=True, max_length=4)
    cidade = models.CharField('Cidade', null=True, max_length=30)
    naturalidade = models.CharField('Naturalidade', null=True, max_length=50)
    email = models.EmailField('Email', null=True, max_length=50)
    facebook = models.CharField('Facebook', null=True, blank=True,  max_length=50)
    frequenta_igreja = models.CharField('Está frequentando alguma igreja?', null=True, max_length=5)
    religiao = models.CharField('Religião', null=True, max_length=30)
    nome_pai = models.CharField('Nome do pai', null=True, blank=True, max_length=60)
    religiao_pai = models.CharField('Religião do pai', null=True, blank=True,  max_length=30)
    nome_mae = models.CharField('Nome da mãe', null=True, max_length=60)
    religiao_mae = models.CharField('Religião da mãe', null=True, blank=True, max_length=30)
    possui_automovel = models.CharField('Possui automóvel?', null=True, max_length=5)
    pessoas_moradia = models.CharField('Quem mora na mesma residência', null=True, max_length=60)
    local_trabalho = models.CharField('Local de trabalho', null=True, blank=True, max_length=40)
    nome_escola = models.CharField('Nome da escola', null=True, blank=True, max_length=60)
    escolaridade = models.CharField('Escolaridade', null=True, blank=True, max_length=40)
    curso = models.CharField('Curso', null=True, blank=False, max_length=50)
    pessoas_participando = models.CharField('Algum conhecido participando do programa?', null=True, max_length=5)
    nome_pessoas_participando = models.CharField('Nome das pessoas', null=True, blank=True, max_length=60)
    possui_probsaude = models.CharField('Possui algum problema de saúde?', null=True, max_length=5)
    nome_probsaude = models.CharField('Qual problema de saúde', null=True, blank=True, max_length=60)
    telefones_urgencia = models.CharField('Telefones para urgência', null=True, max_length=40)
    pessoa_convite_enct = models.CharField('Quem o convidou?', null=True, max_length=40)
    telefone_pessoa_convite = models.CharField('Telefone do encontreiro', null=True, max_length=40)
    desejo_participacao = models.TextField('Porque deseja participar do programa?', null=True)
    pergunta_jesus = models.TextField('Quem é Jesus para você?', null=True)

    STATUS_CHOICES = (
        (0, 'Aguardando Pagamento'),
        (1, 'Concluída'),
        (2, 'Cancelada'),
    )
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
        facebook = self.facebook
        telefones_urgencia = self.telefones_urgencia
        pessoa_convite_enct = self.pessoa_convite_enct
        telefone_pessoa_convite = self.telefone_pessoa_convite
        desejo_participacao = self.desejo_participacao
        pergunta_jesus = self.pergunta_jesus
        msg = 'Nome: {0}\n'\
              'Celular: {1}\nData de nascimento: {2}\n'\
              'CPF: {3}\nEstado civil: {4}\n'\
              'Facebook: {5}\nCidade: {6}\nEstado: {7}\n '\
              'Telefones de emergência: {8}\nQuem o convidou: {9}\nTelefone de quem o convidou: {10}\n'\
              'Porque deseja participar do programa: {11}\nQuem é Jesus para você: {12}\n'\
            .format(nome_apelido, celular, data_nascimento_enc, cpf, estado_civil, facebook,
                    cidade, estado, telefones_urgencia, pessoa_convite_enct,
                    telefone_pessoa_convite, desejo_participacao, pergunta_jesus)
        super(Encontrista, self).save(*args, **kwargs)
        send_mail(
            'INSCRIÇÃO ENCONTRISTA - RJC 2020',
            'Recebemos seus dados em nosso banco de dados\n' + msg + '\n\nPara concluir a inscrição, por favor efetuar o pagamento\n'
                                                                     'Dados bancários: \n'
                                                                     'Agência: 0768\nTipo de conta: 013\nConta: 00045215-5\n'
                                                                     'Banco Caixa Econômica Federal\n'
                                                                     'Favorecida: Jessica Aline Souza Lima\n'
                                                                     'Informações importantes: Não serão aceitos depósitos em envelopes, sob pena de não ser reconhecida a inscrição\n'
                                                                     'Depósitos apenas de forma direta "boca do caixa", lotéricas e/ou transferências bancárias\n\n\n'
                                                                     'Att: Equipe de direção geral - RJC 2020',
            'rjcsantaines@gmail.com',
            [email],
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
    qtd_participantes = models.IntegerField(null=True,  verbose_name='qtd_participantes')
    lider_circulo = models.ForeignKey(Encontreiro, on_delete=models.CASCADE, null=True)
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
            ['rjcsantaines@gmail.com'],
            fail_silently=False,
        )

    def __str__(self):
        return self.nome