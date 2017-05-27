from django.core.management.base import BaseCommand, CommandError
import facebook
from django.conf import settings
from facepy import GraphAPI
from facepy import utils


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # anapaula_token = "EAAPF3KpKPSQBANrm0qH2aBAdS9IhhplrZA8ZCvQai38sp4yMV5AqXZAP2h0A8ZAFO57UPk2k5L78aG13a69062eIZAXZAPeMSpbFRZBjfC6L7Rn3YmBwISMIXZB33IlrM8TmdhxHqj5ZA6XRiEFJzX7fPb6nmbT8UppnuNZAEfZAWIorXy1uhMpFUVWi5MCGUm9qwZC4odoNGdXe7Gv2LZC0cIXcTswQdcxCGkhEZD"

        # graph = GraphAPI(anapaula_token)

        oath_access_token = utils.get_application_access_token(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)

        graph = GraphAPI(oath_access_token)

        users = graph.get('app/accounts/test-users')

        for user in users['data']:
            print ("user", user)
            # print(user['access_token'])
            #graph_user = GraphAPI(user['access_token'])
            friends = graph.get(user['id'])

            print ("friends", friends)

            if "access_token" in user:
                v = GraphAPI(user['access_token'])
                args = {'fields': 'birthday,name'}

                friends = v.get("me/friends", **args)

                print ("friends22", friends)

            print("\n")

        # # Get my latest posts
        # a = graph.get('me/posts')

        # print(a)

        # graph = facebook.GraphAPI(settings.FACEBOOK_APP_ID)
        # print (graph)
        # profile = graph.get_object("User")
        # print (profile)
        # posts = graph.get_connections(profile['id'], 'posts')
