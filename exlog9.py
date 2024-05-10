#Faça um algoritmo para ler três números e se estes poderem formar um triângulo dizer se o triângulo é “EQUILÁTERO”, “ISÓSCELES” OU “ESCALENO”
#                                                      --->CORRIGIR QUESTÃO!<---
print("digite um número A:")
a = float(input())
print("digite outro número B:")
b = float(input())
print("digite um número C:")
c = float(input())
if a == b == c:
    print("Triângulo Equilátero")
elif a == b != c and a == c != b and b == c != a:
     print("Triângulo Isóceles")
elif a != b !=c:
    print("triângulo Escaleno")
    
