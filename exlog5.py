#Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B.
print("digite um número A:")
a = float(input())
print("digite outro número B:")
b = float(input())
if a%b == 0:
    print(f"{a} é divisivel por {b}")
if a%b != 0:
    print(f"{a} não é divisivel por {b}")
    