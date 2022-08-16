import os

class RegistryBookCaseViews:
    def registry_book_case(self) -> str:
        self.__clear()

        print('Criação da Estante \n\n')
        book_case = input('Determine o nome da estante: ')

        return book_case

    def resgistry_book_case_success(self, new_book_case: any) -> None:
        self.__clear()

        message = ''' 
            Estante cadastrada com sucesso!
            * Infos:
                Id da Estante: {}
        '''.format(new_book_case.id, new_book_case.book_case)
        print(message)

    def registry_book_class_fail(self) -> None:
        self.__clear()

        message = ''' 
            Ocorreu um erro ao cadastrar a Estante, confira os campos apresentados
        '''
        print(message)

    def __clear(self):
        os.system('cls||clear')
