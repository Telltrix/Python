# 1) Criar uma lista com 6 notas, ao final realizar a média das notas descartando a primeira e a ultima.
# Mostrar na tela a média
notas= [1,2,3,4,5,6]
soma= 0
count= 1
while count < len(notas)-1:
    soma+= notas[count]
    count+= 1
print(soma/6)
# notas.pop(0)
# notas.pop()
# soma= sum(notas)
# print(soma/6)

# 2) Criar um programa onde o usuario digite 5 numeros inteiros. Ao terminar de digitar os numeros, mostrar
# uma lista somente com numeros impares digitados e a soma desses numeros
impares=[]
for count in range(5):
    numero= int(input(f'Digite o {count+1}º numero: '))
    if numero%2 != 0:
        impares.append(numero)
print(impares)
print(sum(impares))
# lista=[]
# for count in range(5):
#     numero= int(input(f'Digite o {count+1}º numero: '))
#     lista.append(numero)
# lista_impares = [num for num in lista if num % 2 != 0]
# print(lista_impares)


# 3) Fazer um programa que simule uma fila de lotérica. Começar uma lista vazia e dar as seguintes opções:
# A) Entrar pessoa (perguntar o nome)
# B) Saiu pessoa (sempre a que entrou primeiro)
# Se a fila acumular 5 pessoas, finalizar o programa e mostrar a ordem da fila
fila= []
while len(fila) != 5:
    opcao= input('Para adicionar uma pessoa à fila digite 1\nPara remover uma pessoa da fila digite 2\n')
    match opcao:
        case '1':
            fila.append(input('Digite o nome para entrar na fila: '))
            if len(fila) == 5:
                print(f'Fila acumulou 5 pessoas: {fila}')
        case '2':
            fila.pop(0)
        case _:
            print('Valor incorreto')

# 4) Em cidades menores, o alistamento para o exército acontece esporadicamente ao longo dos anos.
# Criar um programa no qual pergunte ao usuário se houve alistamento dos anos 2010 a 2019, uma
# pergunta para cada ano. Se houve alistamento deve ser digitado “S” e se não houve alistamento “N”.
# Após digitar tudo, deve-se mostrar na tela o último ano que houve alistamento. Caso não tenha ocorrido
# alistamento, mostrar “Não houve alistamento nos últimos 10 anos”
alistamento= []
for anos in range(2010, 2020):
    aux= input(f'Se houve alistamento no ano de {anos} digite “S” e se não houve alistamento “N”.')
    if aux.upper() == 'S':
        alistamento.append(anos)
else:
    if len(alistamento) == 0:
        print('Não houve alistamento nos últimos 10 anos')
    else:
        alistamento.reverse()
        print(alistamento[0])

# 5) Desenvolver um programa que peça ao usuário o número de doenças a cadastrar, no qual ele deve
# cadastrar o nome da doença e se ela é transmitida por vírus, bactéria ou por ambos.
# Ao final, mostrar quatro listas: doenças transmitidas por vírus, doenças transmitidas por bactérias, doenças
# transmitidas por ambos, lista com todas doenças.
virus=[]
bacteria=[]
ambas= []
quantidadeDoenças= int(input('Digite a quantidade de doenças a ser cadastrada:'))
for count in range(quantidadeDoenças):
    aux=[]
    aux.append(input('Digite o nome da doença: '))
    tipo= input('Digite 1 - se ela é transmitida por vírus\n2 - se ela é transmitida por bactéria\n3 -se ela é transmitida por ambos\n')
    match tipo:
        case '1':
            virus.extend(aux)
        case '2':
            bacteria.extend(aux)
        case '3':
            ambas.extend(aux)
        case _:
            print('Entrada incorreta')
else:
    print(f'Doenças transmitidas por virus: {virus}')
    print(f'Doenças transmitidas por bactérias: {bacteria}')
    print(f'Doenças trnsmitidas tanto por virus quanto por bactérias: {ambas}')
    todas= virus.copy()
    todas.extend(bacteria)
    todas.extend(ambas)
    print(f'Todas as doenças cadastradas: {todas}')

# 6) Faça um programa em que o usuário digite o nome de 5 produtos e seus preços (“Digite o produto” /
# “Digite o seu preço”) e armazene esses nomes e preços em dois vetores separados. O programa deve
# calcular e mostrar:
# a) A quantidade de produtos com preço inferior a R$50;
# b) O nome dos produtos com preço de R$50 a R$100;
# c) A média dos preços dos produtos com preço superior a R$100.
produto=[]
valor=[]
aux=[]
lowPrice= 0
mediaFInal= 0
hiPrice= 1
media= 0
for count in range(5):
    produto.append(input(f'Digite o nome do {count+1} produto: '))
    valor.append(float(input(f'Digite o valor do {count+1} produto: ')))
    if valor[count] < 50:
        lowPrice+= 1
    if valor[count] >= 50 and valor[count] <= 100:
        aux.append(produto[count])
    if valor[count] > 100:
        media+= valor[count]
        hiPrice+= 1
else:
    mediaFInal= media/hiPrice
    print(f'Produtos abaixo de 50: {lowPrice}')
    print(f'Produtos com preço entre 50 e 100: {aux}')
    print(f'Média dos valores acima de 100: {mediaFInal}')

# 7) Uma sorveteria possui um sistema de self-service de sorvetes no qual o cliente pode montar seu sorvete
# com até 4 bolas (sabores). Criar um programa que simule esse sistema. A montagem do sorvete segue o
# modelo de estrutura PILHA, onde os sabores são "empilhados" um após o outro e quando algum tiver
# que ser removido, será sempre o último da pilha.
# 1- Adicionar sabor
# 2- Remover sabor
# 3- Visualizar sorvete
# 4- Finalizar pedido
# MENSAGENS e VALIDAÇÕES
# Opção 1-> “Sabor adicionado!” OU “Limite de sabores atingido, remova um sabor!”
# Opção 2-> “Sabor removido!” OU “Não existem sabores adicionados!”
# Opção 3-> “Camada 1 - Sabor X, Camada 2 - Sabor Y, etc.” OU “Seu sorvete não possui sabores!”
# Opção 4-> “Pedido realizado!” OU “Adicione pelo menos um sabor!”
# - Criar mensagem de boas vindas e menu funcional.
# - Criar uma lista para a pilha dos sabores.
# - Programar a opção de "Adicionar sabor" corretamente.
# - Programar a opção de "Remover sabor" corretamente.
# - Programar a opção de "Visualizar sorvete" corretamente.
# - Fazer as validações secundárias (lógica).
# - Mostrar mensagens para o usuário (prints).
def listarSabores():
    sabores= ['Morango', 'Manga', 'Uva']
    opcao= input(f'Digite o valor correspondente ao sabor:\n1- {sabores[0]}\n2- {sabores[1]}\n3- {sabores[2]}\n')
    match opcao:
        case '1':
            return sabores[0]
        case '2':
            return sabores[1]
        case '3':
            return sabores[2]
        case _:
            print('Valor incorreto.')
def listarSorvete(sorvete):
    if len(sorvete) == 0:
        print('Seu sorvete não possui sabores!')
    for count in range(len(sorvete)):
        print(f'{count+1}º camada, sabor: {sorvete[count]}')
sorvete=[]
quebra = True
while quebra:
    menu= input(f'Menu da sorveteria digite o valor correspondente a opção:\n1- Adicionar sabor\n2- Remover sabor\n3- Vizualizar sorvete\n4- Finalizar o pedido\n')
    match menu:
        case '1':
            if len(sorvete) == 4:
                print('Limite de sabores atingido, remova um sabor!')
            else:
                sorvete.append(listarSabores())
                print('Sabor adicionado!')
        case '2':
            if len(sorvete) == 0:
                print('Não existem sabores adicionados!')
            else:
                sorvete.pop()
                print('Sabor removido!')
        case '3':
            listarSorvete(sorvete)
        case '4':
            if len(sorvete) == 0:
                print('Adicione pelo menos um sabor!')
            else:
                print('Pedido realizado!')
                quebra = False
        case _:
            print('Valor incorreto')