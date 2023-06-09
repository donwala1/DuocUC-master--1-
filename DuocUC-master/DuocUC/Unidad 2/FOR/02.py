import os
import time
def espera(t):
    time.sleep(t)
os.system("cls")
prom_curso=0
alumno=1

while alumno<=3:
    n1=float(input(f"Ingresa la primera nota del alumno n°{alumno}: " ))
    n2=float(input(f"Ingresa la segunda nota del alumno n°{alumno}: "))

    prom=(n1+n2)/2

    print(f"El promedio de notas del alumno n°{alumno} es: {prom}")
    espera(1)
    prom_curso+=(prom)/alumno
    alumno+=1
    if alumno>3:
        print(f"Promedio curso es:{prom_curso}")
    espera(3)
    os.system("cls")

