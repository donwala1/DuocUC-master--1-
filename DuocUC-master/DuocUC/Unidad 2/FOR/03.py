import os
import time
os.system("cls")

"""3. Crear un programa que lea N vocales (una por una), Después imprimir la información como se
muestra en la tabla de abajo. Esta tabla ejemplifica que se ingresaron 51 vocales, en donde 10
eran A, 6 E, etc. Vocal CANTIDAD A :10 E:6 I:18 O:9 U:8 """

n = int(input("Ingrese el número de vocales: "))

# Inicializar el contador para cada vocal
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

# Leer las vocales una por una y aumentar el contador correspondiente
for _ in range(n):
    vocal = input("Ingrese una vocal: ")
    if vocal == 'A':
        contador_a += 1
    elif vocal == 'E':
        contador_e += 1
    elif vocal == 'I':
        contador_i += 1
    elif vocal == 'O':
        contador_o += 1
    elif vocal == 'U':
        contador_u += 1

# Imprimir la información
print("Vocal  CANTIDAD")
print(f"A      : {contador_a}")
print(f"E      : {contador_e}")
print(f"I      : {contador_i}")
print(f"O      : {contador_o}")
print(f"U      : {contador_u}")