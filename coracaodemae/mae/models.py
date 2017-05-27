from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel, FacebookProfileModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from django.conf import settings
from django.contrib.auth.models import User


class Filho(models.Model):
    sexo_choices = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    nome = models.CharField(max_length=250, verbose_name='Nome')
    sexo = models.CharField(
        max_length=1, choices=sexo_choices, verbose_name="Sexo")
    crianca_especial = models.BooleanField(
        verbose_name="É criança com cuidados especiais")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    alergico = models.CharField(
        max_length=250, verbose_name='Alergias', blank=True)
    doencas = models.TextField(verbose_name='Doenças', blank=True)
    escola = models.CharField(max_length=50, verbose_name="Escola")
    cep_escola = models.IntegerField(max_length=8, verbose_name="Cep Escola")
    natacao = models.BooleanField(verbose_name='Faz natação')
    cep_natacao = models.IntegerField(max_length=8, verbose_name='Cep Natação')
    judo = models.BooleanField(verbose_name='Faz judo')
    cep_judo = models.IntegerField(max_length=8, verbose_name='Cep judo')
    bale = models.BooleanField(verbose_name='Faz bale')
    cep_bale = models.IntegerField(max_length=8, verbose_name='Cep bale')
    ingles = models.BooleanField(verbose_name='Faz ingles')
    cep_ingles = models.IntegerField(max_length=8, verbose_name='Cep ingles')


    def __str__(self):
        return self.nome


class Mae(FacebookProfileModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    teste = models.IntegerField()
    filhos = models.ManyToManyField(Filho)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Mae.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
