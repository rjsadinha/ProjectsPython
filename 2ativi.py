'''Exercício2.
Faça um algoritmo que leia um conjunto indeterminado de números inteiros
e mostre uma mensagem indicando se este número é par ou ímpar, e se é
positivo ou negativo. Terminar o programa quando o numero lido for 0 (Zero).'''

while True:
    numero = int(input("Digite um número inteiro (ou 0 para sair): "))
    if numero == 0:
        break
    
    if numero % 2 == 0:
        par_ou_impar = "par"
    else:
        par_ou_impar = "ímpar"
    
    if numero > 0:
        positivo_ou_negativo = "positivo"
    else:
        positivo_ou_negativo = "negativo"
    
    print(f"O número {numero} é {par_ou_impar} e {positivo_ou_negativo}.")