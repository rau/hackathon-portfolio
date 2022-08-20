import io
import os
from google.cloud import vision
from google.cloud.vision import types

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "apikey.json"

client = vision.ImageAnnotatorClient()


def getLabels(albumid):
    foods = []

    for fileID in os.listdir(albumid):
        file_name = os.path.join(os.path.dirname(__file__), (albumid + '\\' + fileID))
        with io.open(file_name, 'rb') as image:
            content = image.read()

        image = types.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations

        chosenLabel = getOneLabel(labels)
        if chosenLabel:
            foods.append(chosenLabel)

    newFoods = []
    for i in foods:
        if i not in newFoods:
            newFoods.append(i)
    return newFoods

def getOneLabel(labels):
    for label in labels:
        if(label.description.lower() in open('ingredients.txt', 'r').read().lower().split('\n')):
            return label.description
    return ''
