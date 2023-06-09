import os
os.system("cls")

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercero numero: "))

if num1<num2 and num2<num3:
    print("Fueron ingresados de forma creciente")
else:
    print("No fueron ingresados de forma creciente")