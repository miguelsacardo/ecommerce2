from rest_framework import serializers #importando da biblioteca rest_framework os serializers 
from .models import Produto #do arquivo models, importamos a classe Produto (a tabela inteira)

class ProdutoSerializer(serializers.ModelSerializer): #serializers -> de onde vou pegar, Model -> a tabela e o Serializer -> mudar a tabela para JSON
    class Meta: #metadados -> essa classe meta são informações do ProdutoSerializer
        model = Produto
        fields = [ #são os campos, todos que tem na classe Produto
            'id', #o python aceita aspas duplas e simples
            # 'codigoProduto',
            'tituloProduto',
            'preco',
            'descricao',
            'imagemProduto',
            'categoriaProduto',
            'classProduto',
            'exibirHome'
        ]
#fields = '__all__' -> se eu fizer isso, já importo todos os fields

