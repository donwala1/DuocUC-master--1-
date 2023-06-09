from os import system
system("cls")


cars=[]


#auto=[#patente, marca,modelo, año]
'''for i in range(2):
    patente=input("Ingrese patente: ")
    marca=input("Ingrese marca: ")
    modelo=input("Ingrese modelo: ")
    año=input("Ingrese año: ")
    auto=[patente,marca,modelo,año]
    cars.append(auto)'''
    
cars=[['aabb12', 'lada', 'samara', '1980'], ['bbcc34', 'fiat', '600', '4646']]



print(cars[0][2])






print("Buscando datos del automovil")

patente=input("Ingrese patente: ")

for auto in cars:
    if auto[0]==patente:
        print(f"""
            PATENTE: {auto[0]}
            MARCA: {auto[1]} MODELO: {auto[2]}
            AÑO:{auto[3]}
            """)