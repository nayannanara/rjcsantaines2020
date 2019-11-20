from django.contrib import admin
from .models import(
    Encontreiro,
    Encontrista,
    Equipe,
    Circulo,
    Contato
)


class EncontreiroAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf', 'email', 'data_nascimento', 'celular', 'data_cadastro', 'status')
    list_display = ('nome', 'cpf', 'email', 'data_nascimento', 'celular', 'data_cadastro', 'status')
    list_filter = ['data_cadastro', 'status']


class EncontristaAdmin(admin.ModelAdmin):
    search_fields = ('nome_apelido', 'cpf','email', 'data_nascimento_enc', 'celular', 'data_cadastro', 'status')
    list_display = ('nome_apelido', 'cpf', 'email', 'data_nascimento_enc', 'celular', 'data_cadastro', 'status')
    list_filter = ['data_cadastro', 'status']


class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome_equipe', 'get_encontreiros')


admin.site.register(Encontreiro, EncontreiroAdmin)
admin.site.register(Encontrista, EncontristaAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Circulo)
admin.site.register(Contato)