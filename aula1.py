x = 5
y = 5

if(x==y):
    print(f"Os numeros são identicos {x} e {y}")
elif(x>y):
    print(x, " é maior que ", y)
else: 
    print(y, " é maior que ", x)

y = float(input("Digite valor de y: "))
tipo = type(y)
print(tipo)
x = float(input("Digite valor de x: "))
tipo = type(x)
print(tipo)
print(x+y)