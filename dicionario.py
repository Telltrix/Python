# Criar uma variavel pra armazenar informações de um cachorro
list= []
cachorro = {
    'nome': 'Mike',
    'raça': 'chihuahua',
    'idade': 7
}
list.append(cachorro)
print(f'lista aqui {list}')
print(cachorro) 
print(cachorro['raça'])     # verificar o valor da raça
cachorro['castrado'] = True # adicionar nova propriedade
del cachorro['idade']       # excluir propriedade
print(cachorro.keys())      # verificar lista das chaves
print(cachorro.values())    # verificar a lista de valores