def introduction_page():
    message = '''
        Sistema de Cadastro de  Livros e Estantes
        
        * Cadastrar Estante - 1
        * Cadastrar Livros - 2
        * Apresentar livros - 3
        * Sair - 4
    '''

    print(message)
    command = input('Comando: ')
    
    return command 
