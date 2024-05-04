#O indice começa em 1=y, ate 2=z excluindo o 3=m (x, y, z, m)
elementos = ['x','y','z','m']
print(elementos[1:3])

#O for utiliza a lista para  progredir
nomes= ['telmo', "laura"]
for nomes in nomes:
    print(nomes)

#Comando adicionar ao final da lista
nomes=[]
for count in range(6):
    nomes.append(input('Digite nome: '))
    print(f'Nome: {nomes[count]} esta na posição: {count} da lista')

#Comando para adicionar usando index lista.insert(indice, valor)
nomes.insert(2, 'Pedro')

#Comando para atualizar um elemento da lista
nomes[1] = 'Zilma'

#Comando para  remover o ultimo da lista
nomes.pop()

#Comando para remover usando index lista.pop(indice)
nomes.pop(1)

#Comando para remover por valor
nomes.remove('Pedro')

#Comando para remover mais de 1 elemento del lista[x:y]
del nomes[1:2, 3:4]

#Comando para verificar quantidade de um elemento uma lista possui
notas= [5, 6, 7, 6, 7, 8, 6]
print(notas.count(6))

#Comando para encontrar index de um elemento na lista(o primeiro)
print(notas.index(7))

#Comando para adicionar uma lista de itens em uma lista
novas_notas= [11, 12, 14]
notas.extend(novas_notas)
print(notas)

#Comando para ordenar uma lista
notas.sort()

#Comando para reverter uma lista
notas.reverse()

#Comando para limpar a lista
notas.clear()

#Comando para salvar uma lista
notas.copy()

#Comando para listar tamanho
len(notas)
#Comando para listar maior
max(notas)
#Comando para listar menor
min(notas)
#Comando para listar lista ordenada sem mexer nos elementos originais
sorted(notas)
#Comando para retornar uma lista invertida como um objeto iterável(precisa do for)
for item in reversed(notas):
    print(item)

# CRUD
# Create = append
# Read = print
# Update = lista[index] = valor
# Delete = pop, remove
