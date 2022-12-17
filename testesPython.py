##Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
##continue pedindo até que o usuário informe um valor válido.

# nota=float(input("Informe uma nota de 0 a 10", ))
# while nota >10 or nota<0:
#     print("Nota invalida")
#     nota=float(input("Informe uma nota de 0 a 10", ))

##Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
##mostrando uma mensagem de erro e voltando a pedir as informações.

# nome=input("Informe seu usuário: ", )
# senha=input("Informe sua senha: ", )
# while senha==nome:
#     print("Sua senha precisa ser diferente do nome do usuario!")
#     senha=input("Digite uma nova senha:", )

# ##Faça um programa que leia 5 números e informe o maior número

# lista=[]
# for i in range(5):
#     num=input("Informe um numero ", )
#     lista.append(num)

# print(max(lista))

##Faça um programa que receba dois números inteiros e gere os números
##inteiros que estão no intervalo compreendido por eles.

num1=int(input("Informe o numero 1: ", ))

x=0
for i in range(0,10):
    x=(i*num1)
    print(i, 'X', num1, '=', x)
    
