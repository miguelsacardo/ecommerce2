
# class Carro: #nome da classe -> utiliza-se PascalCase
#     def __init__(self,marca,modelo,ano):
#         self.marca = marca #self.marca é global e apenas marca é local
#         self.modelo = modelo
#         self.ano = ano
#         #pass -> quando eu quero que não aconteça nada, usa-se o pass
    
#     def imprimir(self): #o self petence ao objeto . Eu digo que ele é global
#         print(self.marca)

# x = Carro('Toyota', 'Corolla', '2024')
# x.imprimir()

import sqlite3
import pandas as pd

class Ecommerce:
    def __init__(self, db='db.sqlite3'):
       
       #fazer a conexão com banco de dados
       self.conn = sqlite3.connect(db)
       self.menu()

    def menu(self):
        while True:
            print('\n'
                '[1] - Create\n'
                '[2] - Read\n'
                '[3] - Update\n'
                '[4] - Delete\n'
                '[5] - Exit\n\n'
                )
            op = int(input('Escolha uma opção: '))
            match op:
                case(1):
                    print("Create")

                    self.create()
                case(2):
                    self.read()
                case(3):
                    print("Update")
                case(4):
                    print("Delete")
                case(5):
                    break
                case _:
                    print("Opção inválida.")

    def create(self, tituloProduto, preco, descricao, imagemProduto, categoriaProduto, classProduto, exibirHome): #inserir dados no banco
        cursor = self.conn.cursor() #cursor é uma função da conexão, ele que vai executar os comandos do banco

    def read(self):
        print('\n'
              '[1] - Listar todos os produtos\n'
              '[2] - Listar por ID'
              )
        op = int(input("Escolha a opção: "))
        match op:
            case 1: #encontra todos os produtos da tabela e os retorna
                df = pd.read_sql_query('SELECT * FROM api_produto', self.conn)
                return print(df)
            case 2:#enocntra os produtos que possuam um determinado ID
                valor = int(input("ID: "))
                query = f'SELECT * FROM api_produto WHERE id = {valor}'
                df = pd.read_sql_query(query, self.conn)
                return print(df)
            case _:
                print("Escolha uma opção válida...")

    def update(self,  tituloProduto=None, preco=None, descricao=None, imagemProduto=None, categoriaProduto=None, classProduto=None, exibirHome=None):
        #o None serve para que se o nome por exemplo não mudar, ele continuará o mesmo

        cursor = self.conn.cursor()
        campos = []
        valores = []
        
        if tituloProduto:
            campos.append('tituloProduto = ?') #os valores que são diferentes mudarão
            valores.append(tituloProduto)
        
        if preco:
            campos.append('preco = ?')
            valores.append(preco)

        if descricao:
            campos.append('descricao = ?')
            valores.append(descricao)

        if imagemProduto:
            campos.append('imagemProduto = ?')
            valores.append(imagemProduto)

        if categoriaProduto:
            campos.append('categoriaProduto = ?')
            valores.append(categoriaProduto)

        if classProduto:
            campos.append('classProduto = ?')
            valores.append(classProduto)

        if exibirHome is not None: #o exibirHome vale true ou false. ENtão se o exibirHome nao for alterado então ele mantém
            campos.append('exibirHome = ?')
            valores.append(exibirHome)
    
        if campos: #se eu alterei os campos
            valores.append(id) 
            cursor.execute(
                f'''UPDADE api_produto SET {', '.join(campos)} WHERE id = ?''', valores #as três aspas é porque pode ser que tenha mais de uma linha
                )
            self.conn.commit()
            print("Produto atualizado com sucesso")
        else:
            print("Nenhum produto atualizado...")

ecommerce = Ecommerce()
        

