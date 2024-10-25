
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
                    print("Read")
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
        



ecommerce = Ecommerce()
        

