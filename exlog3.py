#Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais
print("digite um número:")
a = float(input())
print("digite outro número:")
b = float(input())
if a > b:
    print(f"{a} é o maior numero e {b} é o menor número")
if b > a:
    print(f"{b} é o maior numero e {a} é o menor número")
if a and b != float or int:
    print("entrada invalida!")