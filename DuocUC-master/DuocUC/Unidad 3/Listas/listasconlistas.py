from os import system
system("cls")


cars=[]

patentes=["AABB12","CCBB23"]
marcas=["LADA","FIAT"]
modelos=["SAMARA","600"]
años=["1985","1970"]

#patente, marca,modelo, año

print("Buscando datos del automovil")

patente=input("Ingrese patente: ")
indice=patentes.index(patente)
print(indice)

print(f"""
      PATENTE: {patentes[indice]}
      MARCA: {marcas[indice]} MODELO: {modelos[indice]}
      AÑO:{años[indice]}
      
      """)
