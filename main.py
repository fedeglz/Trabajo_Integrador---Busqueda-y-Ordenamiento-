from ordenamiento import ordenar_autos_por_marca, ordenar_autos_por_año
from busqueda import busqueda_lineal, busqueda_binaria

#Registramos los Autos
cantidad = int(input("Ingrese la cantidad de autos a registrar: "))

autos = []

for i in range(cantidad):
    print(f"\nRegistro del auto {i+1}:")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    año = int(input("Ingrese el año del auto: "))
    autos.append({"marca": marca, "modelo": modelo, "año": año})


print("\n--------------------------------------")


#ORDENAMIENTO

print("Lista de Autos Original:")
for auto in autos:
    print(auto)

autos_por_marca = autos.copy()
ordenar_autos_por_marca(autos_por_marca)
print("\nAutos Ordenados por Marca:")
for auto in autos_por_marca:
    print(auto)

autos_por_año = autos.copy()
ordenar_autos_por_año(autos_por_año)
print("\nAutos Ordenados por Año:")
for auto in autos_por_año:
    print(auto)


print("\n--------------------------------------")


#BUSQUEDA

# Crear lista simple con nombres de autos para buscar (ej: "Ford Focus")
lista_autos_simple = [f"{auto['marca']} {auto['modelo']}" for auto in autos]

# Búsqueda del usuario
auto_objetivo = input("\nIngrese el auto que desea buscar (ejemplo: Ford Focus): ")

# Búsqueda lineal
pos_lineal = busqueda_lineal(lista_autos_simple, auto_objetivo)
if pos_lineal != -1:
    print(f"\n[Lineal] Auto encontrado en la posición {pos_lineal}: {autos[pos_lineal]}")
else:
    print("\n[Lineal] Auto no encontrado")

# Búsqueda binaria (requiere lista ordenada)
lista_autos_ordenada = sorted(lista_autos_simple)
pos_binaria = busqueda_binaria(lista_autos_ordenada, auto_objetivo)
if pos_binaria != -1:
    print(f"[Binaria] Auto encontrado en la lista ordenada en la posición {pos_binaria}: {lista_autos_ordenada[pos_binaria]}")
else:
    print("[Binaria] Auto no encontrado")