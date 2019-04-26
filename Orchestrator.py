import requests
import json
import getpass


def main():
    print('Olá ' + getpass.getuser() + '!')
    search = input('Por Favor digite o nome de um livro ou uma referência:').replace(':', ' ').split()
    select_tool(search)


def book_request():
    api_json_result_books = requests.get('https://bibleapi.co/api/books/')
    api_dict_result_books = json.loads(api_json_result_books.text)
    return api_dict_result_books


def search_mecanism(book_list, search_for):
    search_at = 0
    search_res = False
    while search_at < len(book_list) and search_res == False:
        if search_for in book_list[search_at].get('name'):
            search_res = book_list[search_at].get('abbrev')
            return search_res
        else:
            search_at = search_at + 1


def text_request(book, chapter, verse):
    api_json_result_text = requests.get('https://bibleapi.co/api/verses/nvi/{}/{}/{}'.format(book, chapter, verse))
    api_dict_result_text = json.loads(api_json_result_text.text)
    print('')
    print(api_dict_result_text.get('text'))


def details_request(book, infs_list):
    api_json_result_infs = requests.get('https://bibleapi.co/api/books/{}'.format(book))
    api_dict_result_infs = json.loads(api_json_result_infs.text)
    for i in infs_list:
        if '0' == i:
            print('O autor desse livro foi {}'.format(api_dict_result_infs.get('author')))
        elif '1' == i:
            if api_dict_result_infs.get('comment') == '':
                print('')
                print('Desculpe esse livro não possui comentários!')
            else:
                print('')
                print('Comentários: {}'.format(api_dict_result_infs.get('comment')))
        elif '2' == i:
            print('')
            print('Esse livro de {} capítulos'.format(api_dict_result_infs.get('chapters')))

        elif '3' == i:
            print('')
            print('Esse livro faz parte do {}'.format(api_dict_result_infs.get('testament')))

        elif '4' == i:
            print('')
            print('Esse livro faz parte do grupo dos {}'.format(api_dict_result_infs.get('group')))


def select_tool(search):
    tools = ['Busca por Referência', 'Busca por Informações']
    print('-----------------------------')
    for i in tools:
        print(tools.index(i), i)
    print('-----------------------------')
    tool = input('Qual ferramenta deseja utilizar?')
    if tool == '0' and len(search) >= 2:
        text_request(search_mecanism(book_request(), search[0]), search[1], search[2])
    elif tool == '1':
        infs_options = ['Autor', 'Comentários', 'Quantidade de Capítulos', 'Testamento', 'Grupo']
        print('-----------------------------')
        for i in infs_options:
            print(infs_options.index(i), i)
        print('-----------------------------')
        infs_list = input('Quais informações você deseja? (Ex: 1,3,4)').split(',')
        details_request(search_mecanism(book_request(), search[0]), infs_list)
    else:
        print('-----------------------------')
        print('Por favor escolha uma opção válida!')
        select_tool(search)


main()
