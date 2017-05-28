from django.core.management.base import BaseCommand
from django.conf import settings
from facepy import GraphAPI
from facepy import utils
from mae.models import Mae


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        oath_access_token = utils.get_application_access_token(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
        graph = GraphAPI(oath_access_token)
        list_users = graph.get('app/accounts/test-users')

        for user in list_users['data']:
            friends = graph.get(user['id'])

            if "access_token" in user:
                v = GraphAPI(user['access_token'])
                args = {'fields': 'name'}
                friends = v.get("me/friends", **args)
                m = Mae.objects.filter(facebook_id=int(user['id']))
                if (m.count() > 0):

                    m = m[0]
                    # m.friends_set.all().delete()

                    # for user_friend in friends['data']:
                    #     m.friends_set.create(nome=user_friend['name'])
                    # m.save()
