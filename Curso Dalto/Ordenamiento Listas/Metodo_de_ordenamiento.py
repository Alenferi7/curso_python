# Metodo de burbujeo
def burbujeo_sort (lista):
    largo = len(lista) - 1

    for i in range(0, largo):
        for j in range (0, largo):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista

# Metodo seleccion
def seleccion_sort(lista):
    largo = len(lista)

    for i in range (0, largo - 1):
        for j in range (i+1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

# Metodo de Insercion
def insercion_sort (lista):
    largo = len(lista)

    for i in range(1, largo):
        aux = lista[i]
        j = i
        while j > 0 and lista[j - 1] > aux:
            lista[j] = lista[j - 1]
            j = j - 1
        lista [j] = aux
    return lista
                
puntos_burbujeo = [45, 70, 32, 100, 53, 52, 99]

puntos_seleccion = [56, 32, 54, 65, 23, 54, 23]

puntos_insercion = [45, 65, 23, 32, 87, 34, 12]

print(f'Estos son los puntos desordenados -> {puntos_burbujeo}')
print('        ↓          ')
print(f'Metodo de burbujeo: {burbujeo_sort(puntos_burbujeo)}')

print('')

print(f'Estos son los puntos desordenados -> {puntos_seleccion}')
print('        ↓           ')
print(f'Metodo de seleccion: {seleccion_sort(puntos_seleccion)}')

print('')

print(f'Estos son los puntos desordenados -> {puntos_insercion}')
print('        ↓           ')
print(f'Metodo de insercion: {insercion_sort(puntos_insercion)}')

