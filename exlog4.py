#Faça um algoritmo para ler um número inteiro e dizer se o número lido é par ou impar.
print("digite um numero inteiro:")
n = int(input())
if n%2 == 0:
    print(f"{n} é par")
if n%2 != 0:
    print(f"{n} é impar")