from django.contrib import admin

# admin.py
from django.contrib import admin
from .models import Cliente, Dispositivo, Profile

# Personalizando a exibição do modelo Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao', 'contato')  # Exibe esses campos na listagem
    search_fields = ('nome', 'localizacao')  # Habilita pesquisa por nome e localização
    list_filter = ('localizacao',)  # Filtro pela localização
    ordering = ('nome',)  # Ordenação por nome

# Personalizando a exibição do modelo Dispositivo
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modelo', 'tipo', 'marca', 'numero_serie', 'cliente')  # Campos na lista
    search_fields = ('nome', 'modelo', 'numero_serie', 'cliente__nome')  # Pesquisa por nome, modelo e cliente
    list_filter = ('tipo', 'marca', 'cliente')  # Filtros para o tipo, marca e cliente
    ordering = ('nome',)  # Ordenação por nome

# Personalizando a exibição do modelo Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')  # Exibe o usuário e o avatar
    search_fields = ('user__username',)  # Permite busca por nome de usuário

# Registrando os modelos e suas classes de administração
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(Profile, ProfileAdmin)

