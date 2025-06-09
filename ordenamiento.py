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

