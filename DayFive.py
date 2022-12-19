#Modulos
import time
import math
import random 

def megasena():
    jogo=[]
    while len(jogo)<6:
        num= random.randint(1,60)
        if num in jogo:
            continue
        else: jogo.append(num)
    print(sorted(jogo))

megasena()

alunos=['Ari', 'Ana', 'Maria', 'João', 'Ivam']
print(random.choice(alunos))
print(random.choice(alunos))

import matplotlib.pyplot as plt