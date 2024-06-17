# Desafio do dia: Cálculo de Bônus com Entrada do Usuário
#Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e 
# informando o valor do salário em comparação com o bônus recebido.

VALOR_BASE= 2000
nome_usuario=input('Digite seu nome: ')
salario_usuario=float(input('Digite seu salario bruto: '))
fator_bonus=float(input('Digite seu fator de bônus: '))
calculo_total=VALOR_BASE + (salario_usuario * fator_bonus)

print(f'Olá {nome_usuario} o valor total do seu bônus é de {calculo_total:.2f}')
