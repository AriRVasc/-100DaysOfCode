#Funções

# Faça uma função que informe a quantidade de dígitos de um
# determinado número inteiro informado.

# def count(n): 
#     digitos=str(n)
#     return len(digitos)

# num = input("Digite uma palavra: ", )
# print(count(num))



def imc(peso, altura):
    calc_imc=peso/(altura*altura)
    return calc_imc

def class_imc(sexo, peso, altura):
    valor_imc=imc(peso, altura)
    if sexo == 'm':
        if valor_imc < 20.7:
            resultado="Você esta abaixo do peso"
        elif valor_imc >= 20.7 and valor_imc<26.4:
            resultado="Você está no peso normal"
        elif valor_imc >= 26.4 and valor_imc<27.8:
            resultado="Você está marginalmente acima do peso"
        elif valor_imc >= 27.8 and valor_imc<=31.1:
            resultado="Você está acima do peso ideal"
        elif valor_imc>31.1:
             resultado="Você está obeso"
        else: resultado="Erro de cálculo, favor contatar o adm."
    elif sexo == 'f':
        if valor_imc < 19.1:
            resultado="Você esta abaixo do peso"
        elif valor_imc >= 19.1 and valor_imc<25.8:
            resultado="Você está no peso normal"
        elif valor_imc >= 25.8 and valor_imc<27.3:
            resultado="Você está marginalmente acima do peso"
        elif valor_imc >= 27.3 and valor_imc<=32.3:
            resultado="Você está acima do peso ideal"
        elif valor_imc>32.3:
             resultado="Você está obeso"
        else: resultado="Erro de cálculo, favor contatar o adm."
    return resultado


print("Olá humana, vamos descobrir seu imc?")
name=input("Digite seu nome: ")

valida_sexo = False

while valida_sexo == False :
    sexo=input("Informe o sexo 'M' ou 'F': ").lower()  
    if sexo != 'm' and sexo != 'f':
        print("Valor inválido, digite 'M' ou 'F'")
        
    else: 
        valida_sexo=True

valida_peso=False

while valida_peso == False :
    peso=input("Informe o seu peso: ")
    try:
        peso=float(peso)
        if peso <=0 or peso >350:
            print("Peso inválido, precisa digitar um valor entre 0 e 350")
        else: valida_peso = True
    except: print("Valor inválido, use apenas números e separe-os com '.'")

valida_altura=False

while valida_altura == False :
    altura=input("Informe a sua altura: ")
    try:
        altura=float(altura)
        if altura <=0 and altura>3.00:
            print("Peso inválido, precisa digitar um valor entre 0 e 3.00")
        else: valida_altura = True
    except: print("Valor inválido, use apenas números e separe-os com '.'")


print("Aqui esta seu resultado "+name+':')
print("Seu imc: ")
print(imc(peso, altura))
print("O resultado dele: ")
print(class_imc(sexo, peso, altura))