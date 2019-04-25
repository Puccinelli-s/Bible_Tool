import requests
import json


def main():
    search_mecanism()


def book_request():
    json_r = requests.get('https://bibleapi.co/api/books/')
    result = json.loads(json_r.text)
    return result


def search_mecanism():
    search = input('O que deseja pesquisar?')
    search_list = search.split(':') and search.split()
    nome = search_list[0]
    lista = book_request()
    for i in lista:
        if nome == i.get('name'):
            abbrev= i.get('abbrev')
            return abbrev


main()
