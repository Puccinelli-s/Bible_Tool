import requests
import json


def main():
    search = input('O que deseja pesquisar?')
    search_list = search.split(':') and search.split()
    search_mecanism(book_request(), search_list[0])

def book_request():
    json_r = requests.get('https://bibleapi.co/api/books/')
    result = json.loads(json_r.text)
    return result


def search_mecanism(list,search_for):
    search_at = 0
    search_res = False
    while search_at < len(list) and search_res == False:
        if search_for in list[search_at].get('name'):
            search_res = list[search_at].get('abbrev')
            return search_res
        else:
           search_at = search_at + 1

main()
