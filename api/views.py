#as views são responsáveis por criar os objetos
from django.shortcuts import render #o render vai sair no HTML
from rest_framework.decorators import api_view #api_view: é um decorator
from .models import Produto #da pasta dos models, importar a tabela de produtos                
from .serializers import ProdutoSerializer #importando do arquivo do "serializers" o serializer
from rest_framework.response import Response #importando a Resposta
from rest_framework import status #fornece constantes que representam os códigos de status do http -> indicam o resultado de uma requisição http

@api_view(['GET', 'POST']) #especificar os tipos de requisição que o método pode usar
def listar_produtos(request): #criei um método 
    if request.method == 'GET': #se o método for 'GET', eu pego todos os dados do model
        queryset = Produto.objects.all() #query é de buscar, set é de incluir. Neste comando, o GET vai no models e pega todos os produtos (objects.all)

        serializer = ProdutoSerializer(queryset, many=True) #many=True serializar todos os modelos do queryset (que está carregando todos os produtos)
        return Response(serializer.data) #resposta que faz parte do return. No final ele dá um return. Este responde dá o serializer.data como resposta 
    
        #o if fora do return quer dizer que ele não irá entrar no escopo do IF acima, mesmo que tivesse identado
    elif request.method == "POST": #se o método for 'POST'
        serializer = ProdutoSerializer(data = request.data) #pegar os dados do formulário (.data)
        if serializer.is_valid(): #se os dados da variável "serializer" forem válidos, ele salva os dados
            serializer.save() #salvar os dados do serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED) #retorna um resultado de requisição do http (sucesso)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) #retorna um resultado de requisição do http (erro)
    

# Create your views here.
