from os import system
system("cls")
alumnos=["jose","lama","208070169"]
asd=False
def prom(a,b,c):
    return float((a+b+c)/3)

while True:
    print(
    """
    ****** MINI SISTEMA DE NOTAS *****

    1. Crear Alumno.
    2. Ingreso de notas de los alumnos
    3. Ver datos del alumno.
    4. Mostrar acta del curso.
    5. Salir
    """)
    op=input("Ingrese una opcion: ")
    match op:
        case "1":
            name=input("Ingerse nombre del alumno: ")
            surname=input("Ingrese el apellido del alumno: ")
            rut=input("Ingrese el rut del alumno: ")
            alumnos_2=[name,surname,rut]
            alumnos.append(alumnos_2)
        case "2":
            while True:
                rut_alumno=input("\nIngrese el rut del alumno: ")
                for alumno in alumnos:
                    if rut_alumno==alumno[2]:
                        nota1=float(input("Ingresa la primera nota: "))
                        nota2=float(input("Ingresa la segunda nota: "))
                        nota3=float(input("Ingresa la tercera nota: "))
                        notas_2=[nota1,nota2,nota3]
                        alumno.append(nota1,nota2,nota3)
                        asd=True
                        break
                if asd==False:
                    print("Ingrese un nombre valido...")
        case "3":
            while True:
                rut_alumno_datos=input("Ingrese el rut del alumno: ")
                if rut_alumno_datos in alumnos:
                    for alumno in alumnos:
                        if alumno[0]==rut_alumno_datos:
                            resultado=prom(alumno[3],alumno[4],alumno[5])
                            print(f"Nombre es: {alumnos[0]}\nApellido: {alumnos[1]}\nRut: {alumno[2]}\nPromedio notas: {resultado} ")
        case other:
            print("asd")
                            