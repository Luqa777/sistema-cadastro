from model import Pessoa, session
from hashlib import sha256
import re

class PessoaController:
    def cadastrar(nome, email, senha):
        if PessoaController.valida_email(email) and PessoaController.validar_senha(senha):
                hash_senha = sha256(senha.encode()).hexdigest()
                try:
                    x = Pessoa(nome, email, hash_senha)
                    session.add(x)
                    session.commit()
                    print('Cadastrado com sucesso')
                except:
                    print('Ocorreu um erro')
        else:
             print('Email invalido ou senha muito longa.')


    def valida_email(email):
        email_existente = session.query(Pessoa).filter_by(email=email).first()
        if email_existente:
            print('email ja cadastrado')
        else:   
            padrao = r'^[\w\.]+@[a-zA-Z\d\.]+\.'
            email_formatado = re.match(padrao, email)
            
            return email_formatado
    
    def validar_senha(senha):
        if len(senha) > 10:
             print('senha muito longa')
        else:
             return senha    
        

class LoginUser:
    def login(email, senha):
        filtra_email = session.query(Pessoa).filter_by(email=f'{email}').first()
        hash_senha = sha256(senha.encode()).hexdigest()
        if filtra_email:
            if hash_senha == filtra_email.senha:
                print('logado com sucesso')
                print(f'bem vindo {filtra_email.nome}')
            else:
                print('senha errada')
        else:
            print('email nao encontrado')