#Faça um algoritmo para ler três números e imprimir se estes podem ou não formar um triângulo.
#Observação – Para formar os lados de um triângulo cada um dos valores tem que ser menor que a soma dos outros dois.
print("digite um número A:")
a = float(input())
print("digite outro número B:")
b = float(input())
print("digite um número C:")
c = float(input())

if a < b+c and b < a+c and c < a+b:
    print("pode formar um triangulo")
else:
    print("não pode formar um triangulo")


    