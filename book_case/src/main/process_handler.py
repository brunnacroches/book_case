from .constructor.introduction_process import introduction_process
# * Cadastrar prateleira
from .constructor.registry_book_case_process import registry_book_case_process
# * Cadastrar livro presente em determinada prateleira
from .constructor.registry_book_process import registry_book_process
# * Apresentar todos os livros presentes em uma prateleira
from .constructor.show_book_process import show_book_process

# * Cadastrar prateleira
# * Cadastrar livro presente em determinada prateleira
# * Apresentar todos os livros presentes em uma prateleira

def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': registry_book_case_process()
        elif command == '2': registry_book_process()
        elif command == '3': show_book_process()
        elif command == '4': exit()
        else: print('\nComando não encontrado, tente novamente!\n\n')
