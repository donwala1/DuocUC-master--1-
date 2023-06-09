import os
os.system("cls")

x=1

while x<=10:
    print(x)
    x+=1


seguir="s"
while seguir=="s":
    seguir=input("Quiere seguir s/n ")
    while seguir not in "sn":
        seguir=input("Ingrese S o N ESTUPIDO!!")

os.system("cls")

while True:
    seguir=input("quiere seguir? s/n").lower()
    if seguir=="n":
        break

