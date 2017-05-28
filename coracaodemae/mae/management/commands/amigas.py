from django.core.management.base import BaseCommand
from mae.models import Mae


def check_igual(mae_origem, mae_destino):
    amigas_iguas = []
    for amiga_origem in mae_origem.friends_set.all():
        print(amiga_origem)
        for amiga_destino in mae_destino.friends_set.all():
            print(amiga_destino)
            if amiga_destino.nome == amiga_origem.nome:
                amigas_iguas.append(amiga_destino.nome)

    print(amigas_iguas)
    return amigas_iguas


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        mae_origem = Mae.objects.get(pk=2)
        mae_destino = Mae.objects.get(pk=3)

        check_igual(mae_origem, mae_destino)
