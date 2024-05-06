# Cadastro de linguagens
lista_linguagens = []
# Repetição quase infinita (break finaliza ela)
while True:
    opcao = int(input('Qual opção você deseja?\n1)Cadastrar linguagem\n2)Listar linguagens\n3)Editar nome de uma linguagem\n4)Excluir uma linguagem\n5)Sair\n'))
    match opcao:
        case 1: # criação (C)
            nome = input('Qual é o nome da linguagem? ')
            lista_linguagens.append(nome)
        case 2: # leitura (R)
            print(lista_linguagens)
        case 3: # edição (U)
            editar = input('Qual é o nome da linguagem que voce quer editar? ')
            indice = lista_linguagens.index(editar)
            novo_nome = input('Qual é o novo nome? ')
            lista_linguagens[indice] = novo_nome
        case 4: # excluir (D)
            indice_exclusao = int(input('Qual é o indice do elemento a ser excluido? '))
            lista_linguagens.pop(indice_exclusao)
        case 5:
            print('Saindo :D')
            break