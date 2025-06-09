# Función de búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Función de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Creamos una lista de autos del 1 al 100
autos = [f"Auto{i}" for i in range(1, 101)]

# Se le pide al usuario que ingrese el auto que quiere buscar
auto_objetivo = input("Ingrese el auto que desea buscar (ejemplo: Auto56): ")

# Busqueda lineal
pos_lineal = busqueda_lineal(autos, auto_objetivo)
if pos_lineal != -1:
    print(f"En la busqueda lineal el auto fue encontrado en la posicion {pos_lineal}")
else:
    print("Auto no encontrado")

# Busqueda binaria
autos_ordenados = sorted(autos)
pos_binaria = busqueda_binaria(autos_ordenados, auto_objetivo)
if pos_binaria != -1:
    print(f"En la busqueda Binaria el auto fue encontrado en la posicion {pos_binaria}")
else:
    print("Auto no encontrado")
