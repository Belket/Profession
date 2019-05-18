from django.db import models
from Test.models import Hint
import re
from pymorphy2 import MorphAnalyzer

# Create your models here.


class HelpFunctions(models.Model):
    class Meta():
        abstract = True

    def is_hint_need(self, text):
        hints = Hint.objects.all()
        defined_words = [hint.defined_word for hint in hints]
        print(defined_words)
        morph = MorphAnalyzer()
        recognized_words = []
        if type(text) == list:
            text = ','.join(text)
        words_of_text = re.split('\.|,|-|\?|\*| ', text)
        normal_words = [morph.normal_forms(word) for word in words_of_text]
        for list_of_normals in range(len(normal_words)):
            for word in normal_words[list_of_normals]:
                if word in defined_words:
                    recognized_words.append(word)
        return recognized_words