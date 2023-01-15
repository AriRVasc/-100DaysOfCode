#aperfeiçoamento de loops


a={'Ana': 10, 'Maria': 28, 'Pedro': 30}

for nome, idade in a.items():
    print(f'{nome} tem {idade} anos. ')


#Buscando a mais velha:
maisVelha=0
for nome, idade in a.items():
    if idade > maisVelha:
        maisVelha=idade

print(f'A pessoa mais velha tem {maisVelha} anos. ')

#Facilitando :
#Mais velha:
print(f'A pessoa mais velha tem {max(a.values())} anos. ')
#Mais nova:
print(f'A pessoa mais velha tem {min(a.values())} anos. ')


