import os
from typing import Dict
# aqui vamos colocar o que o usuário vai ver na tela

class RegistryBookViews:
    def registry_book_view(self) -> Dict:
        self.__clear()

        print('Criação do cadastro do Livro \n\n')
        book = input('Determine o nome do Livro: ')
        book_id = input('Determine o ID do Livro: ')

        return {
            "book": book,
            "book_id": book_id
        }
    
    def registry_book_success(self, new_book: any) -> None:
        self.__clear()

        message = '''
            Livro cadastrado com sucesso!
            * Infos:
                Id da Livro: {}
                Nome do Livro: {}
                Id da Estante: {}
        '''.format(new_book.id, new_book.name, new_book.book_class.id)
        print(message)

    def registry_book_fail(self, error: str) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao cadastrar o livro
        '''.format(error)
        print(message)
        
    def __clear(self):
        os.system('cls||clear')