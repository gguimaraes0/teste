nome = 'stasi'  # string

idade = 14  # inteiro(int)

altura = 1.75 # double 

lista_compras = ["presunto", "pao", "mortadela"] # exemplo de lista
lista_numeros = [8, 4, 1] # exemplo de lista de números


# item = lista_compras[0] + " e " + lista_compras[2]
# print(item)

# dados_pessoa = [{"nome": "Joao", "Idade": 40, "Altura": 1.80}, {"nome": "Maria", "Idade": 17, "Altura": 1.65}]

# print(dados_pessoa[0])

# tupla_coordenadas = (50,20,5)

def calculaCompras(precomortadela, precopao, precoleite):
    pagamento = precoleite + precopao + precomortadela
    return pagamento

def dobra(valor):
    return valor*2

precoleite = 5
precopao = 1
precomortadela = 6

pagamento = 0
pagamento = calculaCompras(precoleite, precopao, precomortadela)
print(pagamento)
pagamento = dobra(pagamento)

print(pagamento)




# if (pagamento > 10):
#     print('Está liberado passar no cartão de crédito')
# elif (pagamento == 50):
#     print('Não vou vender')
# elif (pagamento == 50):
#     print('Não vou vender denovo')
# else:
#     print('Não está liberado passar no cartão de crédito')
