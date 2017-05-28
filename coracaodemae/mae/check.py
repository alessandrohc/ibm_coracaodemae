from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3
from pprint import pprint


def check_image(caminho):
    visual_recognition = VisualRecognitionV3(
        '2016-05-20', api_key='99dd359a09fc08737086e737094478d2aae44689')

    file_path = join(dirname(__file__), caminho)
    with open(file_path, 'rb') as image_file:
        results = visual_recognition.detect_faces(images_file=image_file)
        for obj in results['images']:
            for i in obj['faces']:
                if i['gender']['gender'] == 'FEMALE':
                    return True
                else:
                    return False
