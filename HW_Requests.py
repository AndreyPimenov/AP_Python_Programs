
# Работа с API Yandex.Переводчик
# -------------------------------------------------------------------------
# Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:
# Путь к файлу с текстом;
# Путь к файлу с результатом;
# Язык с которого перевести;
# Язык на который перевести (по-умолчанию русский)
# -------------------------------------------------------------------------

import os
import requests

URL = 'https://translate.yandex.net/api/v1/tr.json/translate?'
# обратите внимание, что %s -ru потому что переводим с иностранных на русский язык
params ='id=56261fc2.5cf6aa29.9dd20577-0-0&srv=tr-touch&lang=%s'
in_out_lang = '%s'

def translate(text_for_translate, in_out_lang):
    ''' Эта функция принимает переменные:
        текст для перевода, язык текста и язык на который нужно перевести
        И возвращает переведенный текст '''
    response = requests.post(URL, data={'text': text_for_translate}, params=params %in_out_lang)
    body = response.json()
    print(response.text)
    print(response.status_code)
    try:
        return(body['text'])
    except KeyError:
        print(body['message'])


def readfile(filename, in_out_lang):
    ''' Эта функция считывает файл построчно,
    переводит каждую и сохраняет результ
    в отдельной строковой переменной'''
    try:
        abstract = str()
        with open(filename+'.txt') as f:
            for line in f:
                abstract = abstract + str(translate(line, in_out_lang))
    except FileNotFoundError:
        print("Название файла вы ввели неправильно")
    return abstract


def savetext(text, file_to):
    ''' Преобразует результат предыдущих функций
    и записывает в новый текстовый файл'''
    sentence = str()
    with open(file_to, 'w') as f:

        # Очистка строкового файла от ненужных символов:
        del_sim = str("\[]''")
        for char in del_sim:
            text = text.replace(char,'')
            print(text)

        # подсчет кол-ва предложений
        num_sentences = text.count('.', 0, len(text)) + 1
        print('кол-во предложений: ', num_sentences)

        for num_sentences in text:
            stop_in = text.find('.')
            if stop_in != (-1):
                print(stop_in)

                sentence = text[0:(stop_in+1)] # +1 потому что точку вклчюаем в перевод
                f.write(sentence)

                text = text[(stop_in+2)::]
            else:
                break

def text_translate():#file_from, file_to, lang_in, lang_out):
    file_from = input('Укажите путь к файлу с текстом для перевода')
    file_to = input('Укажите путь к файлу для сохранения текста')
    lang_in = input('двумя строчными буквами укажите язык текста оригинала')
    lang_out = input('двумя строчными буквами укажите язык текста перевода')

    in_out_lang = lang_in + '-' + lang_out

    if readfile(file_from, in_out_lang) == str():
        print ("Запустите программу снова")
    else:
        text = readfile(file_from, file_to)
        savetext(text, in_out_lang)



if __name__ == '__main__':

    text_translate()


