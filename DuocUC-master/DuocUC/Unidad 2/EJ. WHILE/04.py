import os
os.system("cls")

num1=int(input("Ingresa un numero: "))
num2=int(input("Ingresa otro numero: "))

print("""
      1. SUMA
      2. RESTA
      3. MULTIPLICACION
      4. DIVISION
      """)

opcion=int(input("Seleccion una operacion: "))
os.system("cls")

match opcion:
    case 1:
        res=num1+num2
    case 2:
        res=num1-num2
    case 3:
        res=num1*num2
    case 4:
        rest=num1/num2
    case other:
        print("Opcion no valida")



