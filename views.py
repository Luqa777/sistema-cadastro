from controller import PessoaController, LoginUser
login = False

while login == False:
    print('1 - Cadastrar \n2 - Logar')
    escolha = input('Escolha: ')
    if escolha == '1':
        nome = input('nome: ')
        email = input('email: ')
        senha = input('senha: ')
    
        try:
            PessoaController.cadastrar(nome, email, senha)
        except:
            print('views error')

    if escolha == '2':
        email = input('email: ')
        senha = input('senha: ')
    
        try:
            LoginUser.login(email, senha)
        except:
            print('erro')