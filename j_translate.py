from os import *
from microsofttranslator import Translator
cid = 'circleline10'
cse = 'WLNfAKP5FD0y4SNH5/g8Macw3z8rjO8S2w1kH5CH4Gg='

translator = Translator(cid, cse)
lang_dict = {}
def add_to_dict(lang, name, key):
    lang_dict.setdefault(lang, [name, key])
    print(lang_dict)

#initial = {'thai': ['Kanya', 'th'], 'german': ['Anna', 'de'], 'greek': ['Melina', 'el'], 'arabic': ['Tarik', 'ar'], 'swedish': ['Alva', 'sv'], 'russian': ['Milena', 'ru'], 'norwegian': ['Nora', 'no'], 'dutch': ['Ellen', 'nl'], 'czeck': ['Zuzana', 'cs'], 'slovak': ['Laura', 'sk'], 'danish': ['Sara', 'da'], 'hungarian': ['Mariska', 'hu'], 'french': ['Thomas', 'fr'], 'turkish': ['Yelda', 'tr'], 'polish': ['Zosia', 'pl'], 'chinese': ['Ting-Ting', 'zh-CHT'], 'romanian': ['Ioana', 'ro'], 'spanish': ['Monica', 'es'], 'italian': ['Alice', 'it'], 'japanese': ['Kyoko', 'ja'], 'portugese': ['Joana', 'pt'], 'indonesian': ['Damayanti', 'id'], 'finnish': ['Satu', 'fi'], 'korean': ['Yuna', 'ko'], 'hindi': ['Lekha', 'hi'], 'hebrew': ['Carmit', 'he']}

#l_dict = {'thai': ['Kanya', 'th'], 'german': ['Anna', 'de'], 'greek': ['Melina', 'el'], 'arabic': ['Tarik', 'ar'], 'swedish': ['Alva', 'sv'], 'russian': ['Milena', 'ru'], 'norwegian': ['Nora', 'no'], 'dutch': ['Ellen', 'nl'], 'czeck': ['Zuzana', 'cs'], 'slovak': ['Laura', 'sk'], 'danish': ['Sara', 'da'], 'hungarian': ['Mariska', 'hu'], 'french': ['Thomas', 'fr'], 'turkish': ['Yelda', 'tr'], 'polish': ['Zosia', 'pl'], 'chinese': ['Ting-Ting', 'zh-CHT'], 'romanian': ['Ioana', 'ro'], 'spanish': ['Monica', 'es'], 'italian': ['Alice', 'it'], 'japanese': ['Kyoko', 'ja'], 'portugese': ['Joana', 'pt'], 'indonesian': ['Damayanti', 'id'], 'finnish': ['Satu', 'fi'], 'korean': ['Yuna', 'ko'], 'hindi': ['Lekha', 'hi'], 'hebrew': ['Carmit', 'he']}
final_dict = {'greek': ['Melina', 'el', 'el-GR'], 'norwegian': ['Nora', 'no', 'nb-NO'], 'portugese': ['Joana', 'pt', 'pt-PT'], 'german': ['Anna', 'de', 'de-DE'], 'polish': ['Zosia', 'pl', 'pl-PL'], 'chinese': ['Ting-Ting', 'zh-CHT', 'cmn-Hans-CN'], 'hindi': ['Lekha', 'hi', 'hi-IN'], 'finnish': ['Satu', 'fi', 'fi-FI'], 'japanese': ['Kyoko', 'ja', 'ja-JP'], 'russian': ['Milena', 'ru', 'ru-RU'], 'french': ['Thomas', 'fr', 'fr-FR'], 'czeck': ['Zuzana', 'cs', 'cs-CZ'], 'arabic': ['Tarik', 'ar', 'ar-SA'], 'indonesian': ['Damayanti', 'id', 'id-ID'], 'swedish': ['Alva', 'sv', 'sv-SE'], 'turkish': ['Yelda', 'tr', 'tr-TR'], 'slovak': ['Laura', 'sk', 'sk-SK'], 'hebrew': ['Carmit', 'he', 'he-IL'], 'hungarian': ['Mariska', 'hu', 'hu-HU'], 'korean': ['Yuna', 'ko', 'ko-KR'], 'romanian': ['Ioana', 'ro', 'ro-RO'], 'spanish': ['Monica', 'es', 'es-ES'], 'italian': ['Alice', 'it', 'it-IT'], 'danish': ['Sara', 'da', 'da-DK'], 'thai': ['Kanya', 'th', 'th-TH'], 'dutch': ['Ellen', 'nl', 'nl-NL']}

def append_dict():
    for k,v in l_dict.items():
        code = input('language: {0}\n'.format(k))
        l_dict[k].append(code)
    
    

def translate(text, language):
    x = translator.translate(text, final_dict[language][1])
    print(x)
    system("say -v {0} {1}.".format(final_dict[language][0], x))
    pass
    
