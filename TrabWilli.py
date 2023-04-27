import os
import pandas as pd

tabela = pd.read_csv("C:\\Users\\luccasilva\\Downloads\\DNIT-Distancias.csv")
#print(tabela)
#tabela_total = pd.DataFrame()
'''
# tabela_total = tabela_total.append(tabela)
print(tabela_total)
'''
'''
# Criando um DataFrame de exemplo
data = {'Nome': ['Maria', 'João', 'Ana', 'Pedro'],
        'Idade': [25, 30, 27, 35],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']}

df = pd.DataFrame(data)

# Localizando um item na tabela
cidade1 = input()
cidade2 = input()

# Localizando linhas com Nome igual a 'João' E Cidade igual a 'Rio de Janeiro'
resultado = df.loc[(df['Nome'] == cidade1) & (df['Cidade'] == cidade2)]

print(resultado)
'''
# Lendo a planilha Excel em um DataFrame do pandas
df = pd.read_csv('C:\\Users\\luccasilva\\Downloads\\DNIT-Distancias.csv')

# Localizando um item na planilha
nome = input('Digite a 1° cidade:  ')
cidade = input('Digite a 2° cidade:  ')

# Localizando linhas com Nome igual a 'João' E Cidade igual a 'Rio de Janeiro'
resultado = df.loc[(df['Nome'] == nome) & (df['Cidade'] == cidade)]

print(resultado)