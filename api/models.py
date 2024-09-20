from django.db import models


class Produto(models.Model):
    codigoProduto = models.IntegerField(max_length=10) #IntegerField = campo de número inteiro, max_length -> o campo aceita até tantos caracteres
    tituloProduto = models.CharField(max_length=255) #CharField = campo de caracteres
    preco = models.DecimalField(max_length=10, decimal_places=2) #DecimalField = campo de decimal, decimal_places = quantas casas decimais queremos
    descricao = models.TextField(max_lenght=500)
    imagemProduto = models.CharField(max_length=255) #a imagem por enquanto vai ser salva em CharField
    categoriaProduto = models.CharField(max_length=255)
    classProduto = models.CharField(max_length=255)
    exibirHome = models.BooleanField(default=True) #define um padrão para o campo Bool como True