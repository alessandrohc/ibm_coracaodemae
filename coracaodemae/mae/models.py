from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from django.conf import settings

# Create your models here.
class Imagens(models.Model):
    image = models.ImageField(upload_to="uploads")

    def __str__(self):
        return self.image.name


class Mae(FacebookModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    @receiver(post_save)
    def create_profile(sender, instance, created, **kwargs):
        """Create a matching profile whenever a user object is created."""
        if sender == get_user_model():
            user = instance
            profile_model = get_profile_model()
        if profile_model == Mae and created:
            profile, new = Mae.objects.get_or_create(user=instance)


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
