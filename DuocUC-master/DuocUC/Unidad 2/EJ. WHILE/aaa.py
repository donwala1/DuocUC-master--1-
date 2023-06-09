import os
os.system("cls")
tipo=(input(
"""
SELECCIONE UN CILINDRO:
1. 5 KILOS (5.000)
2. 11 KILOS (12.000)
3. 15 KILOS (18.000)
4. 45 KILOS (38.000)

"""))
os.system("cls")
despacho=(input("""
SELECCIONE UN LUGAR DE DESPACHO:
1. CONCEPCION (2.000)
2. TALCAHUANO (3.000)
3. HUALPEN (2.500)
"""))
os.system("cls")
descuento=(input("""
BENEFICIO DE DESCUENTO:
1. CAJA LOS ANDES
2. CAJA LOS HEROES
3. SIN DESCUENTO
"""))



os.system("cls")
match tipo:
    case "1":
        valor_cilindro=5000
        tipo_cilindro="5 KILOS"
    case "2":
        valor_cilindro=12000
        tipo_cilindro="11 KILOS"
    case "3":
        valor_cilindro=18000
        tipo_cilindro="15 KILOS"
    case "4":
        valor_cilindro=38000
        tipo_cilindro="45 KILOS"
    case other:
        print("Ingrese un valor valido por favor")

match despacho:
    case "1":
        valor_despacho=2000
        lugar_despacho="CONCEPCION"
    case "2":
        valor_despacho=3000
        lugar_despacho="TALCAHUANO"
    case "3":
        valor_despacho=2500
        lugar_despacho="HUALPEN"
    case other:
        print("Ingrese un lugar valido")
match descuento:
    case "1":
        caja="CAJA LOS ANDES"
        res=(valor_cilindro+valor_despacho)*0.9
    case "2":
        caja="CAJA LOS HEROES"
        res=(valor_cilindro+valor_despacho)*0.95
    case "3":
        caja="SIN DESCUENTO"
        res=(valor_despacho+valor_cilindro)
    case other:
        print("Ingrese un valor valido por favor")
os.system("cls")
print(
f"""
**** RESUMEN DE LA COMPRA ****
GAS: {tipo_cilindro}
DESCUENTO: {caja}
DESPACHO A: {lugar_despacho}
TOTAL: {round(res*1.19)}
VALOR PAGADO EN IVA: {round(res*0.19)}

""")

