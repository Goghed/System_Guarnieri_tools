from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Cliente", blank=True, null=True)
    localizacao = models.CharField(max_length=200, verbose_name="Localização", blank=True, null=True)
    contato = models.CharField(max_length=20, verbose_name="Contato", blank=True, null=True)  # Opcional

    def __str__(self):
        return self.nome
        

class Dispositivo(models.Model):
    TIPO_CHOICES = [
        ('Câmera', 'Câmera'),
        ('DVR', 'DVR'),
        ('NVR', 'NVR'),
        ('Outro', 'Outro'),
    ]
    MARCA_CHOICES = [
        ('Hikvision', 'Hikvision'),
        ('Dahua', 'Dahua'),
        ('Intelbras', 'Intelbras'),
        ('Outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome do Dispositivo", blank=True, null=True)
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name="Tipo", default='Outro')
    numero_serie = models.CharField(max_length=100, unique=True, verbose_name="Número de Série")
    firmware = models.CharField(max_length=100, verbose_name="Firmware", blank=True, null=True)
    marca = models.CharField(max_length=50, choices=MARCA_CHOICES, verbose_name="Marca", default='Outro')
    ip = models.CharField(max_length=15, verbose_name="Endereço IP", default='0.0.0.0')
    submask = models.CharField(max_length=15, verbose_name="Submask", default='255.255.255.0')
    gateway = models.CharField(max_length=15, verbose_name="Gateway", default='0.0.0.0')
    porta_http = models.IntegerField(verbose_name="Porta HTTP", default=80)
    porta_servico = models.IntegerField(verbose_name="Porta Serviço", default=8000)
    porta_rtsp = models.IntegerField(verbose_name="Porta RTSP", default=554)
    usuario = models.CharField(max_length=50, verbose_name="Usuário", default='admin')
    senha = models.CharField(max_length=50, verbose_name="Senha", default='1234')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='dispositivos', verbose_name="Cliente")

    def __str__(self):
        return f"{self.nome} ({self.marca} - {self.modelo})"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='images/avatars/default-avatar.jpg')

    def __str__(self):
        return f"Profile of {self.user.username}"
    

# Cria um perfil automaticamente quando um usuário é criado
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        

# Salva o perfil automaticamente quando o usuário é salvo
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    profile, created = Profile.objects.get_or_create(user=instance)
    profile.save()