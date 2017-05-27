from django.db import models
from django_facebook.models import FacebookProfileModel
from django.conf import settings


class Mae(FacebookProfileModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)


class Filho(models.Model):
    sexo_choices = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    mae = models.ForeignKey(Mae)

    nome = models.CharField(max_length=250, verbose_name='Nome')
    sexo = models.CharField(
        max_length=1, choices=sexo_choices, verbose_name="Sexo")
    crianca_especial = models.BooleanField(
        verbose_name="É criança com cuidados especiais")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    alergico = models.CharField(
        max_length=250, verbose_name='Alergias', blank=True)
    doencas = models.TextField(verbose_name='Doenças', blank=True)
    escola = models.CharField(max_length=50, verbose_name="Escola", blank=True)
    cep_escola = models.IntegerField(verbose_name="Cep Escola", blank=True, null=True)
    natacao = models.BooleanField(verbose_name='Faz natação')
    cep_natacao = models.IntegerField(verbose_name='Cep Natação', blank=True, null=True)
    judo = models.BooleanField(verbose_name='Faz judo')
    cep_judo = models.IntegerField(verbose_name='Cep judo', blank=True, null=True)
    bale = models.BooleanField(verbose_name='Faz bale')
    cep_bale = models.IntegerField(verbose_name='Cep bale', blank=True, null=True)
    ingles = models.BooleanField(verbose_name='Faz ingles')
    cep_ingles = models.IntegerField(verbose_name='Cep ingles', blank=True, null=True)

    def __str__(self):
        return self.nome
