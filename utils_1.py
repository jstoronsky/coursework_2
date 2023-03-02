import requests
import random
from homework_9.class_Basicword import BasicWord
index = random.randint(0, 2)


def load_random_word():
    """
    загружаем с сайта список слов для игры и создаём экземпляр класса BasicWord
    """
    response = requests.get("https://www.jsonkeeper.com/b/ILP8")
    response_json = response.json()
    python_words = response_json[index]
    basicword2 = BasicWord(python_words["word"], python_words["subwords"])
    return basicword2
