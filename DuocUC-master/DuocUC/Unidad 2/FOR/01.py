import os
import time

os.system("cls")
while True:
    a=int(input("Ingresa un numero: "))
    b=int(input("Ingresa otro numero: "))

    if a<b:
        for num in range(a,b+1):
            print(num)
    else:
        print("INGRESA UN NUMERO A MAYOR PIMERO AWNAO")
    time.sleep(3)
    os.system("cls")


