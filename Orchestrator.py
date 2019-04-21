import requests
import json


def Main():
    search_mecanism()


def book_request():
    json_r = requests.get('https://bibleapi.co/api/books/')
    result = json.loads(json_r.text)
    return result


def search_mecanism():
    search = input('O que deseja pesquisar?')
    search_list = search.split(':') and search.split()
    search_result = book_request().index(search_list[0])
    print(search_result)


Main()
