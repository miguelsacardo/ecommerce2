from django.db import models


class Produto(models.Model):
    tituloProduto = models.CharField(max_length=255) #CharField = campo de caracteres
    preco = models.DecimalField(max_digits=10, decimal_places=2) #DecimalField = campo de decimal, decimal_places = quantas casas decimais queremos, max_digits = quantos digitos poderão ser digitados
    descricao = models.TextField(max_length=500)
    imagemProduto = models.CharField(max_length=255) #a imagem por enquanto vai ser salva em CharField
    categoriaProduto = models.CharField(max_length=255)
    classProduto = models.CharField(max_length=255)
    exibirHome = models.BooleanField(default=True) #define um padrão para o campo Bool como True