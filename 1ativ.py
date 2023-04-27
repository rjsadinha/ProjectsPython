'''
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%,
escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo
ao consumidor'''



carro = float(input('Digite o valor do carro para ver o valor final: '))
imposto = carro*45/100
valor_dist = carro*28/100
valor_final = carro + imposto + valor_dist
print('Esse e o valor do imposto',imposto)
print('Esse e o valor do distribuidor:',valor_dist)
print('Este e o valor final que o consumidor ira pagar no carro: ', valor_final)