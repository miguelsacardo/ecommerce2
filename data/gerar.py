import pandas as pd #importa a biblioteca Pandas e chama ela como "pd" -> trata a planilha como se fosse uma tabela
import os #importa os comandos do sistema operacional

data = {
    'tituloProduto':['furadeira','bomba'],
    'preco':[400, 1500],
    'descricao':['Fura bem', 'Bomba combustível'],
    'imagemProduto':['/image','/image'],
    'categoriaProduto':['Ferramentas', 'Auto'],
    'classProduto':['Casa', 'Carro'],
    'exibirHome':[True, False]
}

df = pd.DataFrame(data) #atribui a variável df um arquivo que será convertido em data frame
caminho_atual = os.getcwd() #current word director(cwd)
caminho_final = caminho_atual.replace('\\', '/') #o replace é usado para substituir as "\" do caminho para "/" pro python conseguir interpretar

df.to_csv(caminho_final + '/data/ferramentas.csv', index=False) #converte o dataframe para CSV e salva no caminho especificado     index=false -> se eu não colocar isso, ele vai querer criar outra coluna de index
