#Tuplas -> São imutáveis

meses=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#se eu tentar alterar irá dar erro:
#meses[0]='Dezembro'
#print(meses[0])


#Listas -> podem ser alteradas
alunos=['Maria', 'João', 'Ana', 'Miguel']

#e possivel alterar qualquer elemento:
alunos[0]='Helena'
print(alunos[0])
#posso acrescentar elemento no final da lista:
alunos.append('Ricardo')
print(alunos)

#posso acrescentar elemento no indice da lista q eu preferir, informa primeiro o indice, depois o elemento:
alunos.insert(2,'Ari')
print(alunos)

#ordenando a lista por ordem alfabética:
alunos.sort()
print(alunos)

#remover elemento da lista através do indice
alunos.pop(1)
print(alunos)

#remover elemento da lista pelo nome do elemento:
alunos.remove('Ana')
print(alunos)

#podemos concatenar duas ou mais listas
alunos2=['Joana', 'Jorge']

todosAlunos=alunos+alunos2
print(todosAlunos)

#Exercício Mes de nascimento
data_nasc=input('Digite a data de nascimento no formato DD-MM-AA: ', )
mes=data_nasc[3:5]
print(mes)
mesX=int(mes)
print(type(mesX))


print('Voce nasceu no mes de:', meses[mesX-1])

#Dicionarios

ari={'sobrenome': 'Rodrigues', 'idade': '28', 'profissão': 'programadora python', 
'filhos':['Snoop Dog', 'Pequeno']}
del ari['idade']
print(ari)

print('sobrenome' in ari)

for x in ari:
    print(x)

print(ari.get('nome', 'Esta informação nao consta no cadastro'))

ari['filhos'].append('Brisa')
print(ari)

#limpar todo os valores dos itens do dicionario
ari.clear()
print(ari)

#Exercicio Dicionario de cores em ingles

cores={'Verde':'Green', 'Amarelo': 'Yellow', 'Azul':'Blue'}
cor=input('Digite uma cor: ', )

print(cores.get(cor, 'Esta informação nao consta no cadastro'))

fimPrograma=input('Aperte qualquer tecla para finalizar.', )