from os import system
from time import sleep
system("clear")
contactos=[]
while True:
    borrado=False
    system("clear")
    print("\t\t\t*****BIENVENIDOS A LA APLICACION DE CONTACTOS DONWALITA*****\n1) Agregar Contacto\n2) Eliminar Contacto\n3) Ordenar Contactos Alfabeticamente\n4) Mostrar lista de contactos\n5) Salir.")
    op=input("Seleccione una opcion: ")
    match op:
        case "1":
            while True:
                system("clear")
                name=input("Ingrese el nombre del contacto: ").lower()
                if len(name)>0 and name.isalpha():
                    break
                else:
                    print("Ingrese un nombre valido...")
                    input("Presione ENTER para continuar")
                    
            while True:
                system("clear")
                surname=input("Ingrese el apellido del contacto: ").lower()
                if len(surname)>0 and surname.isalpha():
                    break
                else:
                    print("Ingrese un apellido valido...")
                    input("Presione ENTER para continuar")
            while True:
                system("clear")
                try:    
                    age=int(input("Ingrese la edad del contacto: "))
                    if age > 0 and age < 140:
                        break
                except ValueError:
                    print("Ingrese una edad valida por favor...")
            while True:
                system("clear")
                num=input("Ingrese el numero de telefono del contacto: ")
                if len(num)==9 and num.isnumeric:
                    break
                else:
                    print("Ingrese un numero valido por favor...")
                    input("Presione ENTER para continuar")
            contactos_2=[name,surname,age,num]
            contactos.append(contactos_2)
            system("cls")
            input("Contacto agregado correctamente.\n\nPresione ENTER para continuar")
        case "2":
            while True:
                system("clear")
                delet=input("Ingrese el nombre del contacto que desea eliminar: ").lower()
                for i, contacto in enumerate(contactos):
                    if contacto[0]==delet:
                        contactos.remove(contactos[i])
                        borrado=True
                        system("clear")
                        print("Contacto eliminado correctamente")
                        input("Presione enter para continuar")
                if borrado==False:
                    print("Ingrese un contacto valido por favor...")
                    input("Presiona ENTER para continuar")
                break
        case "3":
            system("clear")
            contactos.sort()
            print("Los contactos se han ordenado de forma alfabetica correctamente")
            input("Presione enter para continuar")
        case "4":
            system("cls")
            for contacto in contactos:
                print(
                    f"""
                    ********************************
                        NOMBRE: {contacto[0]}
                        APELLIDO: {contacto[1]}
                        EDAD: {contacto[2]}
                        N° TELEFONO: {contacto[3]}
                    ********************************
                    """)
            input("\nPresione ENTER para continuar")
        case "5":
            system("cls")
            print("Hasta luego! ")
            input("Presione ENTER para salir del programa")
            break
        case other:
            system("cls")
            print("Ingrese una opcion correcta por favor...")
            sleep(2)