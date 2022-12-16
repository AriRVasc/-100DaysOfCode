#Condicionais

#Exercicio if, elif, else
'''
nome=input('Digite o nome do aluno: ', )
nota1=float(input('Digite a nota 1 do aluno: ', ))
nota2=float(input('Digite a nota 2 do aluno: ', ))
faltas=int(input('Informe quantas faltas o aluno tem: ', ))

media=(nota1+nota2)/2
assiduidade=(20-faltas)/20


if media < 6 and assiduidade <0.7:
    resultado="Reprovado por faltas e por média!"
    
elif media>=6 and assiduidade<0.7:
    resultado= "O aluno foi reprovado por faltas"

elif media<6 and assiduidade>=0.7:
   resultado="O aluno foi reprovado por media"

elif media>=6 and assiduidade>=0.7:
    resultado="O aluno foi aprovado"


print("O nome do aluno é: ",nome)
print("A media do aluno foi: ",media)
#colocando porcentagem:
print("O indice de presença do aluno foi: ",str(assiduidade*100)+'%')
print("O resultado foi: ",resultado)

'''
#Teste de Loop While

'''
x=0
alunos=[]

while x<4:
    nome=input("Informe o nome de um aluno:")
    if nome=='joao':
        continue

    if nome=='maria':
        break

    alunos.append(nome)
    x+=1

print(alunos)

'''

#Exercicio  Fatura:

usuario=input("Informe o nome do usuario: ", )
fatura=[]
total=0
x='s'
while x == 's':
    produto=input("Informe o nome do produto que deseja: ", )
    preco=float(input("Informe o valor do produto: ", ))
 
    fatura.append([produto, preco])
    total+=preco

    x=input("Deseja comprar mais alguma coisa? s ou n", ).lower()
    
for i in fatura:
    print(i[0], i[1])

print('O total da compra foi: ',total)
