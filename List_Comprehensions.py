lista_preco=[1000, 20000, 3000, 4000, 500, 600,7000]

#dobrar o valor da lista
#Para cado preco acima de 1000 o imposto, imposto de 50% sobre o valor

novo_preco=[ preco*2 for preco in lista_preco ]
print(novo_preco)

preco_imposto=[ int(preco2*1.5) for preco2 in lista_preco if preco2>1000]
print(preco_imposto)

