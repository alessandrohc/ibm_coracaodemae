from django.core.management.base import BaseCommand
from watson_developer_cloud import VisualRecognitionV3
from watson_developer_cloud import LanguageTranslatorV2, PersonalityInsightsV3
from mae.models import Mae
import json
import numpy as np


def load_insights(content):
    personality_insights = PersonalityInsightsV3(
        version='2016-10-20',
        username="6e84e48a-fc9a-4d98-b300-44e4c8fde1c7",
        password="rbZEPiu5aEu0")

    profile = personality_insights.profile(content, content_type='text/plain',
                                           raw_scores=True, consumption_preferences=True)

    result = {}
    result_name = []
    result_values = []
    for obj in profile['personality']:
        if "children" in obj:
            for _obj in obj['children']:
                result[_obj['trait_id']] = _obj['raw_score']
                result_name.append(_obj['trait_id'])

    result_name = sorted(result_name)

    for key in result_name:
        result_values.append(result[key])

    return result_values


def check_image(file_path):
    visual_recognition = VisualRecognitionV3(
        '2016-05-20', api_key='99dd359a09fc08737086e737094478d2aae44689')

    with open(file_path, 'rb') as image_file:
        results = visual_recognition.detect_faces(images_file=image_file)
        for obj in results['images']:
            if 'faces' in obj:
                for i in obj['faces']:
                    if i['gender']['gender'] == 'FEMALE':
                        return True
                    else:
                        return False
            else:
                return False


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        api_key = '99dd359a09fc08737086e737094478d2aae44689'

        language_translator = LanguageTranslatorV2(
            username='b28b4c7e-f7b2-454d-ac93-07fb878f79c9',
            password='umwRwmafJEpF')

        # traducao = language_translator.translate(texto, source='en', target='pt-br')
        result = []
        result_ids = []
        for mae in Mae.objects.all().order_by("pk"):

            mae.ibm_verificado_mulher = check_image(mae.foto_mae_pq.path)
            mae.save()

            result_ids.append(mae.pk)
            texto = mae.get_all_posts()
            # texto = "obrigado"

            params = {
                "source": "pt-br",
                "target": "en",
                "text": texto
            }

            # traducao = language_translator.translate(texto, source='pt-br', target='en')
            # traducao = language_translator.translate(json.dumps(params))
            traducao = texto
            result.append(load_insights(traducao))

        cor = np.array(result)
        corrcoef = np.corrcoef(cor)

        for i in range(len(result_ids)):
            mae_order = {}

            for j in range(len(result_ids)):
                mae_order[result_ids[j]] = corrcoef[i][j]

            _m = Mae.objects.get(pk=result_ids[i])
            _m.ibm_personalidade = json.dumps(mae_order)
            _m.save()
