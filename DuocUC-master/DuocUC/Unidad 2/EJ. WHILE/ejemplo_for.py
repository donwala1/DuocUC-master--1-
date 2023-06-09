from os import system
system("cls")

for i in range(10):
    print(i, end=" ")

print("\n")
for i in range(1,11):
    print(i, end=" ")

print("\n")
for i in range(2,11,2):
    print(i, end=" ")

print("\n")
for i in range(10,0,-1):
    print(i, end=" ")

print("\n")

palabra="paralelepipedo"
print("\n")
for letra in range(len(palabra)):
    print(letra, end="-")
print("\n")
print(len(palabra))
for letra in palabra:
    print(letra, end="-")
