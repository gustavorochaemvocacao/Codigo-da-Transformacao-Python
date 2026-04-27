'''
1.criar expressoes matemáticas usando oeradores aritméticos

2.Escrever um programa que peça 2 numeros ao usuario  e mostre qual é o maior 

3. implementar uma estreutura if-elif-else que classifica a idade de uma pessoa 
'''
#1
soma = 5 + 3
subtracao = 5 - 3
multiplicacao = 5 * 3
divisao = 5 / 3
print('soma: ' + str(soma))
print('subtração: ' + str(subtracao))
print('multiplicação: ' + str(multiplicacao))
print('divisão: ' + str(divisao))



#2
print('digite o primeiro numero')
numero1 = int(input())
print('digite o segundo numero')
numero2 = int(input())
if numero1 > numero2:
    print('o maior numero é: ' + str(numero1))
elif numero2 > numero1:
    print('o maior numero é: ' + str(numero2))
else:
    print('os numeros são iguais')


#3
print('Digite a idade da pessoa:')
idade = int(input())
if idade < 13:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 40:
    print('Adulto')
else: 
    print('Idoso')


