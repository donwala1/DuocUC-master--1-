import os
os.system("cls")
alumnos=["matias","jose"]
"""Agregar objeto lista"""

alumnos.append("Wacoldo")
alumnos.append("Diogenes")
alumnos.append("Juanito")
#con len
#for i in range(len(alumnos)):
#     print(alumnos[i])


#con forreach
#for alumno in alumnos:
#    print(alumno)

"""eliminar un objeto lista"""
alumnos.remove("Prudencio")
alumnos.remove(alumnos[2])


"""Buscar objeto en la lista"""
encontrado=False
buscando="Pelayo"
for i in range(len(alumnos)):
    if buscando==alumnos[i]:
        encontrado=True
        print("Lo pille")
        break
if encontrado==False:
    print("No encontrado")

"""Buscar en coleccion"""

if "Pelayo" in alumnos:
    print("Lo encontre")
else:
    print("No lo encontre")

alumnos.insert(2,"tertulia")