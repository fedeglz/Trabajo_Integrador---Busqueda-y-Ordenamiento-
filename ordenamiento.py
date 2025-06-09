autos = []

cantidad = int(input("Ingrese la cantidad de autos a registrar: "))

for i in range(cantidad):
    print(f"\nRegistro del auto {i+1}:")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    año = int(input("Ingrese el año del auto: "))
    autos.append({"marca": marca, "modelo": modelo, "año": año})
print("--------------------------------------")

#Ordenar autos por marca(Bubble Sort)
def ordenar_autos_por_marca(autos):
    n = len(autos)
    for i in range(n):
        for j in range(0, n-i-1):
            if autos[j]["marca"] > autos[j+1]["marca"]:
                autos[j], autos[j+1] = autos[j+1], autos[j]
    

#Ordenar autos por año(Selection Sort)
def ordenar_autos_por_año(autos):
    n = len(autos)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if autos[j]["año"] < autos[min_index]["año"]:
                min_index = j
        autos[i], autos[min_index] = autos[min_index], autos[i]


#Probar las funciones de ordenamiento
print("Lista de Autos Original:")
for auto in autos:
    print(auto)

#Ordenar por marca
autos_por_marca = autos.copy()
ordenar_autos_por_marca(autos_por_marca)
print("\nAutos Ordenados por Marca:")
for auto in autos_por_marca:
    print(auto)

#Ordenar por año
autos_por_año = autos.copy()
ordenar_autos_por_año(autos_por_año)
print("\nAutos Ordenados por Año:")
for auto in autos_por_año:
    print(auto)

