import os

class ShowBookViews:
    def show_book_view(self) -> str:
        self.__clear()

        print('Busca de Livros  \n\n')
        book_name = input('Determine o nome do livro para busca: ')

        return book_name
    
    def show_book_success(self, book_registry: any) -> None:
        self.__clear()

        message = '''
            Número de Registro do Livro
            * Infos:
                Id do Livro: {}
                Nome do Livro: {}
        '''.format(
            book_registry["id"],
            book_registry["name"],
        )
        print(message)
    
    def show_book_failt(self, error: str) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao buscar o livro.
            {}
        '''.format(error)
        print(message)

    def __clear(self):
        os.system('cls||clear')
