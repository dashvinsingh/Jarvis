from os import *
from microsofttranslator import Translator
cid = 'circleline10'
cse = 'WLNfAKP5FD0y4SNH5/g8Macw3z8rjO8S2w1kH5CH4Gg='

translator = Translator(cid, cse)
lang_dict = {}
def add_to_dict(lang, name, key):
    lang_dict.setdefault(lang, [name, key])
    print(lang_dict)

l_dict = {'thai': ['Kanya', 'th'], 'german': ['Anna', 'de'], 'greek': ['Melina', 'el'], 'arabic': ['Tarik', 'ar'], 'swedish': ['Alva', 'sv'], 'russian': ['Milena', 'ru'], 'norwegian': ['Nora', 'no'], 'dutch': ['Ellen', 'nl'], 'czeck': ['Zuzana', 'cs'], 'slovak': ['Laura', 'sk'], 'danish': ['Sara', 'da'], 'hungarian': ['Mariska', 'hu'], 'french': ['Thomas', 'fr'], 'turkish': ['Yelda', 'tr'], 'polish': ['Zosia', 'pl'], 'chinese': ['Ting-Ting', 'zh-CHT'], 'romanian': ['Ioana', 'ro'], 'spanish': ['Monica', 'es'], 'italian': ['Alice', 'it'], 'japanese': ['Kyoko', 'ja'], 'portugese': ['Joana', 'pt'], 'indonesian': ['Damayanti', 'id'], 'finnish': ['Satu', 'fi'], 'korean': ['Yuna', 'ko'], 'hindi': ['Lekha', 'hi'], 'hebrew': ['Carmit', 'he']}
def append_dict():
    for k,v in l_dict.items():
        code = input('language: {0}'.format(l_dict[k]))
        d[k].append(code)
    
    

def translate(text, language):
    x = translator.translate(text, l_dict[language][1])
    print(x)
    system("say -v {0} {1}.".format(l_dict[language][0], x))
    return None
    
