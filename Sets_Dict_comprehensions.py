""" with open ('texto.txt', 'r') as t:
    texto = t.read()

print(texto)

def func(texto):
    '''Retornar dict
    dict[char]= quantidade em que char aparece em texto'''
    chars = []
    quantity = []
    for c in texto:
        if not c in chars:
            chars.append(c)
            quantity.append(1)
        else: 
            index = chars.index(c)
            quantity[index] += 1
    
    d={}

    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d

funcao=func(texto)
print(funcao)
 """
## Utilizando Sets  :

with open ('texto.txt', 'r') as t:
    texto = t.read()

def func(texto):
    '''Retornar dict
    dict[char]= quantidade em que char aparece em texto'''
    chars = set()
    for c in texto:
        chars.add(c)
    chars= list(chars)
    quantity = [texto.count(c) for c in chars]

    d={}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d

funcao=func(texto)
print(funcao)


## Utilizando Lists :

def func3(texto):
    '''Retornar dict
    dict[char]= quantidade em que char aparece em texto'''
    chars = list({c for c in texto})
    quantity = [texto.count(c) for c in chars]

    d={}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d

funcao=func3(texto)
print(funcao)

#melhorias:

def func4(texto):
    '''Retornar dict
    dict[char]= quantidade em que char aparece em texto'''
    chars = list({c for c in texto})
    quantity = [( c, texto.count(c)) for c in chars ]
    return dict(quantity) 

print(func4(texto))

#Utilizando Collections:

def func5(texto):
    '''Retornar dict
    dict[char]= quantidade em que char aparece em texto'''
    return dict([(c, texto.count(c)) for c in set(texto)])

print(func5(texto))


#Utilizando Dict Comprehension:

def func6(texto):
    '''Retornar dict
    dict[char]= quantidade em que char aparece em texto'''
    return { c: texto.count(c) for c in set(texto)}

print(func6(texto))

