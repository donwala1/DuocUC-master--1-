from os import system
from random import randint
system("cls")

def suerte():
    return randint(1,100)

def salud():
    print("Holaa!!!")

def calcular(a,b):
    return (a+b)



def saludarconnombre(nombre:str):
    print(f"Hola {nombre}")
while True:
    print(
        """
        1. Saludar
        2. Saludar con nombre
        3. Numero de la suerte
        4. Salir
        """)
    op=input("Ingrese una opcion: ")

    match op:
        case "1":
            salud()
        case "2":
            nom=input("Ingresa nombre")
            saludarconnombre(nom)
        case "3":
            num=suerte()
            print("Su numero de la suerte es: ",num)
        case "4":
            n1=int(input("Ingresa un numero: "))
            n2=int(input("Ingresa otro numero: "))
            resultado=int(calcular(n1,n2))

            print(f"El resultado es: ",resultado)



