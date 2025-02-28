from django import forms
from .models import Cliente, Dispositivo
from django.contrib.auth.models import User
from clientes.models import Profile  

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'localizacao', 'contato']

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'  # Ou liste os campos manualmente se quiser excluir algum


class CadastroUsuarioForm(forms.Form):
    nome = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)
    tecnicos = forms.BooleanField(required=False)
    suporte = forms.BooleanField(required=False)
    administrativo = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('confirmar_senha', "As senhas não coincidem.")

        return cleaned_data
    

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, required=False)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput, required=False)
    foto_perfil = forms.ImageField(required=False)  # Campo para upload da foto

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('confirmar_senha', "As senhas não coincidem.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        # Se uma senha foi informada, setamos corretamente
        if self.cleaned_data["senha"]:
            user.set_password(self.cleaned_data["senha"])

        if commit:
            user.save()
            # Salvar a foto no Profile
            if "foto_perfil" in self.cleaned_data and self.cleaned_data["foto_perfil"]:
                profile, created = Profile.objects.get_or_create(user=user)
                profile.avatar = self.cleaned_data["foto_perfil"]
                profile.save()

        return user

