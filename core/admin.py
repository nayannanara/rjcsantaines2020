from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import(
    Circulo,
    Encontreiro,
    Encontrista,
    Contato,

)


class EncontreiroAdmin(ImportExportModelAdmin):
    search_fields = ('nome', 'cpf', 'email', 'idade', 'celular', 'data_cadastro', 'status')
    list_display = ('nome', 'cpf', 'email', 'idade', 'celular', 'data_cadastro', 'status')
    list_filter = ['data_cadastro', 'status']
    list_per_page = 50
    ordering = ['nome']


class EncontristaAdmin(ImportExportModelAdmin):
    search_fields = ('nome_apelido', 'cpf','email', 'data_nascimento_enc', 'celular', 'data_cadastro', 'status')
    list_display = ('nome_apelido', 'cpf', 'email', 'data_nascimento_enc', 'celular', 'data_cadastro', 'status')
    list_filter = ['data_cadastro', 'status']
    list_per_page = 50
    ordering = ['nome_apelido']


class EquipeAdmin(ImportExportModelAdmin):
    list_display = ['nome_equipe', 'get_encontreiros', 'qtd_participantes', 'nome_coordenador', 'nome_casal_ligacao']


class CirculoAdmin(ImportExportModelAdmin):
    list_display = ['nome_circulo', 'get_encontristas', 'qtd_participantes', 'lider_circulo', 'cor_equipe']
    fields = ('nome_circulo', 'encontristas')


class ContatoAdmin(ImportExportModelAdmin):
    list_display = ['nome', 'email', 'telefone']


class EquipeAzulAdmin(ImportExportModelAdmin):
    list_display = ['encontrista_name', 'encontrista_celular', 'lider_circulo']

    def encontrista_name(self, instance):
        return str(instance.encontristas.nome_apelido)

    def encontrista_celular(self, instance):
        return str(instance.encontristas.celular)


admin.site.register(Encontreiro, EncontreiroAdmin)
admin.site.register(Encontrista, EncontristaAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Circulo, CirculoAdmin)