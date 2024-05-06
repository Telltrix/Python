# Criar um CRUD simples, utilizando listas, métodos (e keywords, caso necessite), para armazenamento de usuários em uma lista
# chamada lista_de_cadastros
# Exemplo:
# 1) Cadastrar usuário
# 2) Editar usuário
# 3) Excluir usuário
# 4) Listar usuários
# 5) Sair
def cadastraUsuarios():
    usuario= {}
    usuario['nome']= input('Digite o nome do usuário: ')
    usuario['idade']= int(input('Digite a idade do usuário: '))
    usuario['email']= input('Digite o e-mail do usuário: ')
    return usuario

def listaUsuario(listaCadastrada):
    for count in range(len(listaCadastrada)):
        aux= listaCadastrada[count]
        print(f'Nome: {aux['nome']} idade: {aux['idade']} e-mail: {aux['email']}')
    
def encontraUsuario(listaCadastrada, nome):
    for count in range(len(listaCadastrada)):
        aux= listaCadastrada[count]
        if nome.lower() == aux['nome']:
            return count

lista_de_cadastros= []
exit= True
while exit:
    opcao = int(input('Qual opção você deseja?\n1)Cadastrar usuário\n2)Editar usuário\n3)Excluir usuário\n4)Listar usuário\n5)Sair\n'))
    match opcao:
        case 1:
            lista_de_cadastros.append(cadastraUsuarios())
            print('Usuário cadastrado com sucesso!')
        case 2:
            listaUsuario(lista_de_cadastros)
            nome= input('Digite o nome do usuário que você quer editar:\n')
            lista_de_cadastros.pop(encontraUsuario(lista_de_cadastros, nome))
            lista_de_cadastros.append(cadastraUsuarios())
            print('Usuário editado com sucesso!')
        case 3:
            listaUsuario(lista_de_cadastros)
            nome= input('Digite o nome do usuário que você quer excluir:\n')
            lista_de_cadastros.pop(encontraUsuario(lista_de_cadastros, nome))
            print('Usuário excluido com sucesso!')
        case 4:
            listaUsuario(lista_de_cadastros)
        case 5:
            exit= False
        case _:
            print('Opção incorreta')



# Criar um CRUD, utilizando dicionários para armazenamento de animais de um petshop em uma lista chamada lista_de_animais
# Exemplo:
# 1) Cadastrar pet (dicionário com nome e espécie)
# 2) Editar pet
# 3) Excluir pet
# 4) Listar pets
# 5) Listar pets de uma espécie informada pelo usuário
# 6) Sair

def cadastraPet():
    pets= {}
    pets['nome']= input('Digite o nome do pet: ')
    pets['idade']= int(input('Digite a idade do pet: '))
    pets['especie']= input('Digite a espécie do pet: ')
    return pets

def listaPets(listaCadastrada):
    for count in range(len(listaCadastrada)):
        aux= listaCadastrada[count]
        print(f'Nome: {aux['nome']} idade: {aux['idade']} espécie: {aux['especie']}')
    
def encontraPet(listaCadastrada, nome):
    for count in range(len(listaCadastrada)):
        aux= listaCadastrada[count]
        if nome.lower() == aux['nome']:
            return count
        
def listaEspecie(listaCadastrada, especie):
    ren= True
    for count in range(len(listaCadastrada)):
        aux= listaCadastrada[count]
        if especie.lower() == aux['especie']:
            print(f'Nome: {aux['nome']} idade: {aux['idade']} espécie: {aux['especie']}')
            ren= False
    if ren: 
        print('Nenhum pet da espécie foi encontrado')

lista_de_animais= []
exit= True
while exit:
    opcao = int(input('Qual opção você deseja?\n1)Cadastrar pet\n2)Editar pet\n3)Excluir pet\n4)Listar pets\n5)Listar pets por espécie\n6)Sair\n'))
    match opcao:
        case 1:
            lista_de_animais.append(cadastraPet())
            print('Pet cadastrado com sucesso!')
        case 2:
            listaPets(lista_de_animais)
            nome= input('Digite o nome do Pet que você quer editar:\n')
            lista_de_animais.pop(encontraPet(lista_de_animais, nome))
            lista_de_animais.append(cadastraPet())
            print('Pet editado com sucesso!')
        case 3:
            listaPets(lista_de_animais)
            nome= input('Digite o nome do Pet que você quer excluir:\n')
            lista_de_animais.pop(encontraPet(lista_de_animais, nome))
            print('Pet excluido com sucesso!')
        case 4:
            listaPets(lista_de_animais)
        case 5:
            especie= input('Digite a espécie à ser listada:\n')
            listaEspecie(lista_de_animais, especie)
        case 6:
            exit= False    
        case _:
            print('Opção incorreta')