from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from clientes.forms import ClienteForm, DispositivoForm
from clientes.models import Profile
from django.contrib.auth.models import User
from clientes.forms import CadastroUsuarioForm, UsuarioForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'clientes/login.html')

@login_required
def dashboard(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    avatar_url = profile.avatar.url if profile.avatar else 'images/avatars/default-avatar.jpg'

    context = {
        'user_name': user.get_full_name() or user.username,
        'avatar_url': avatar_url,
    }
    return render(request, 'clientes/dashboard.html', context)

@login_required
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastrar_cliente.html', {'form': form})

@login_required
def cadastrar_dispositivo(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DispositivoForm()
    return render(request, 'clientes/cadastrar_dispositivo.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')


@login_required
def cadastrar_usuario(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)

            # Se uma nova senha foi fornecida, precisamos criptografá-la
            if form.cleaned_data["senha"]:
                user.set_password(form.cleaned_data["senha"])

            user.save()

            # Atualizar a foto de perfil, se uma nova imagem foi enviada
            if "foto_perfil" in request.FILES:
                profile.avatar = request.FILES["foto_perfil"]
                profile.save()

            return redirect('dashboard')

    else:
        form = UsuarioForm(instance=user)

    avatar_url = profile.avatar.url if profile.avatar else 'images/avatars/default-avatar.jpg'

    context = {
        'form': form,
        'user_name': user.get_full_name() or user.username,
        'avatar_url': avatar_url
    }

    return render(request, 'clientes/cadastrar_usuario.html', context)

