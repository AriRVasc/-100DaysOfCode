print('Hello World')
nome='Ariadne'
sobrenome_meio='Rodrigues'
ultimo_sobrenome= 'Vasconcelos'
nome_completo=nome+' '+sobrenome_meio+' '+ultimo_sobrenome
print(nome_completo)
print(len(nome_completo))

print(nome[2:])
print(nome[:2])

iniciais= nome[0]+' '+sobrenome_meio[0]+' '+ultimo_sobrenome[0]
print(iniciais)

empresa="Ari Tecnology"
email=nome+ultimo_sobrenome+'@'+empresa +'.com'
print(email)

num=10
num2=9.5
print(type(num))
print(type(num2))

print(5>2)

idade=28
if idade >=18:
    print("Acesso Liberado")
else: print("Acesso negado")

import math

print(math.factorial(num))

print("Digite no numero do dia do desafio #100DaysOfCode em que voce esta:")
day_desafio=int(input())
print("Voce esta no dia:",day_desafio)

print('Fim do Programa')
