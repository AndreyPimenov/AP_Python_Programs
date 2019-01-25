# Работа с API Yandex.Переводчик
# -------------------------------------------------------------------------
# Расширить функционал
# В классе мы напишем функцию-переводчик.
# Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:
# Путь к файлу с текстом;
# Путь к файлу с результатом;
# Язык с которого перевести;
# Язык на который перевести (по-умолчанию русский)
# -------------------------------------------------------------------------
# Алгоритм (инвариантный к названию файла, желательно в случае небольшого размера исходного файла)
# 1. выбрать с каким файлом работаем
# 2. открываем этот файл его содержимое сохраняем в переменной text
# 3. закрываем файл
# 4. справшиваем с какого языка переводим
# 5. закидываем в яндекс переводчик text
# 6. создаем новый файл с именем: 'ch_lang'_RU.txt
# 7. записываем в этот файл переменную text
# 8. закрываем файл
# Выдает ошибку 413: слишком "тяжелый" запрос, поэтому пошел другим путем:
# -------------------------------------------------------------------------

import requests
URL = 'https://translate.yandex.net/api/v1/tr.json/translate?'
# обратите внимание, что %s -ru потому что переводим с иностранных на русский язык
params = 'id=162bbc6f.5c4363cb.833e8bb0-2-0&srv=tr-text&lang=%s'
in_out_lang = '%s'
#        'id=162bbc6f.5c4363cb.833e8bb0-2-0&srv=tr-text&lang=%s-ru' - для сети в кафе
#        'id=a5763280.5c237e4a.bb5ce734-11-0&srv=tr-text&lang=%s-ru' - для сети в универе

def translate(text_for_translate, in_out_lang):
    ''' Эта функция принимает переменные: текст для перевода, язык текста и язык на который нужно перевести
        И возвращает переведенный текст '''
    response = requests.post(URL, data={'text': text_for_translate}, params=params %in_out_lang)
    body = response.json()
    #print(response.text)
    #print(response.status_code)
    try:
        return(body['text'])
    except KeyError:
        print(body['message'])

def readfile(filename, in_out_lang):
    ''' Эта функция считывает файл построчно, переводит каждую и сохраняет результ в отдельной строковой переменной'''
    try:
        abstract = str()
        with open(filename+'.txt') as f:
            for line in f:
                abstract = abstract + str(translate(line, in_out_lang))
    except FileNotFoundError:
        print("Название файла вы ввели неправильно")
    return abstract

def savetext(text, in_out_lang):
    ''' Преобразует результат предыдущих функций и записывает в новый текстовый файл'''
    sentence = str()
    with open(in_out_lang, 'w') as f:

        # Очистка строкового файла от ненужных символов:
        del_sim = str("\[]''")
        for char in del_sim:
            text = text.replace(char,'')
            print(text)
        # подсчет кол-ва предложений 
        num_sentences = text.count('.', 0, len(text)) + 1
       
        for num_sentences in text:
            stop_in = text.find('.')
            if stop_in != (-1):
                print(stop_in)
                sentence = text[0:(stop_in+1)] # +1 потому что точку вклчюаем в перевод
                f.write(sentence)
                text = text[(stop_in+2)::]
            else:
                break

if __name__ == '__main__':
     in_lang = input('Введите язык с которого хотите перевести')
     out_lang = input('Введите язык на который хотите перевести')
     in_out_lang = in_lang + '-' + out_lang

     filename = input('Введите название файла')
     if readfile(filename, in_out_lang) == str():
         print ("Запустите программу снова")
     else:
         text = readfile(filename, in_out_lang)
         savetext(text, in_out_lang)
