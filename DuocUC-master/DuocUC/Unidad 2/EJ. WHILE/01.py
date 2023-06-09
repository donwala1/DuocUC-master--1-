import os
os.system("cls")


sueldo=int(input("Ingrese sueldo trabajador: "))
if sueldo>=1000:
    print(f"Su sueldo es: {sueldo}\nsu sueldo con aumento es: {sueldo * 1.15}")
else:
    print(f"Su sueldo es: {sueldo}")