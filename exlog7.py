#Faça um algoritmo para ler três números e imprimir o maior.
print("digite um número A:")
a = float(input())
print("digite outro número B:")
b = float(input())
print("digite um número C:")
c = float(input())
if a > b and c:
    print("o maior número é:",a)
elif b>= a and b>=c:
    print("o maior número é:",b)
else:
    print("o maior número é:",c)