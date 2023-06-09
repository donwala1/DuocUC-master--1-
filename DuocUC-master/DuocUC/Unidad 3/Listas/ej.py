import os
os.system("cls")
amigos=[]
while True:
    print("""
    1. Agregar Amigos
    2. Buscar Amigos
    3. Eliminar Amigos
    4. Ordenar amigos en orden alfabetico
    5. Mostrar amigos
    """)
    op=input("Selecciona una opcion: ")
    os.system("cls")
    match op:
        case "1":
            while True:
                add=input("Ingrese el nombre del amigo: ")
                if len(add)>0:
                    break
            amigos.append(add)
            while True:
                other_friend=input("¿Desea agregar otro amigo?\n1. Si\n2. No\n:")
                if other_friend=="1":
                    add=input("Ingrese el nombre del amigo: ")
                    amigos.append(add)
                elif other_friend == "2":
                    os.system("cls")
                    break
        case "2":
            while True:
                bus=input("Ingresa el nombre de la persona que estas buscando: ")
                if bus in amigos:
                    print("Si se encuentra")
                    find_other=input("¿Desea buscar otro contacto?\n1. Si\n2. No\n:")
                    if find_other=="1" or "2":
                        if find_other=="2":
                            break
                    else:
                        print("Ingresa una opcion correcta")
                else:
                    print("No se encuentra")
                    break
        case "3":
            print(amigos)
            elim=input("¿Que amigo quieres eliminar?")
            if elim in amigos:
                amigos.remove(elim)
        case "4":
            amigos.sort()
            for amigo in amigos:
                print(amigo,end=",")
            num=1
            input("\nAprete enter para continuar")
        case "5":
            for amigo in amigos:
                print(amigo,end=",")
            input("\nAprete enter para continuar")
        case other:
            print("Ingrese una opcion correcta n.n")