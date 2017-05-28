from django.core.management.base import BaseCommand
from mae.models import Mae


def check_igual(mae_origem, mae_destino):
    igual_atributos = []
    print(mae_origem.filho_set.all())
    for filho_origem in mae_origem.filho_set.all():
        print(filho_origem.escola)
        for filho_destino in mae_destino.filho_set.all():
            print(filho_destino.cep_escola)
            if filho_origem.cep_escola == filho_destino.cep_escola:
                igual_atributos.append('escola')
            if filho_origem.cep_bale == filho_destino.cep_bale:
                igual_atributos.append('bale')
            if filho_origem.cep_natacao == filho_destino.cep_natacao:
                igual_atributos.append('natacao')
            if filho_origem.cep_ingles == filho_destino.cep_ingles:
                igual_atributos.append('ingles')
            if filho_origem.cep_judo == filho_destino.cep_judo:
                igual_atributos.append('judo')
            if filho_origem.sexo == filho_destino.sexo:
                igual_atributos.append('sexo')

    if (mae_origem.animal_estimacao == mae_destino.animal_estimacao):
        igual_atributos.append('animal_estimacao')
    if mae_origem.bairro == mae_destino.bairro:
        igual_atributos.append('bairro')

    print(igual_atributos)
    return igual_atributos


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        mae_origem = Mae.objects.get(pk=2)
        mae_destino = Mae.objects.get(pk=3)

        print(check_igual(mae_origem, mae_destino))
