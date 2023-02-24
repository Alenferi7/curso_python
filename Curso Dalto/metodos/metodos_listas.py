#1. Metodos de listas

lista = ['holis', 'alen', 'alendi', 72, True]
print(lista)

#1.01 len() -> devuelve la cantidad de elementos que de la lista

largo_lista = len(lista)
print(largo_lista)

#1.02 .append() -> agrega un elemento a la lista (lo agrega en el ultimo indice)

lista.append('agumon')
print(lista)

#1.03 .insert(indice, elemento) -> agrega un elemento a la lista de un indice especifico
'''como un append pero yo indico donde ira ubicado el elemento'''

lista.insert(2, 'elend')
print(lista)

#1.04 .extend([lista, lista1, lista2]) -> agrega varios elementos a la lista.

lista.extend(['Marcos', 'Miles', 9])
print(lista)

#1.05 .pop() -> elimina un elemento de la lista (por su indice), si no
#expecificamos, elimina el ultimo indice.

lista.pop()
print(lista)

#1.06 .remove -> elimina un elemneto de la lista, no se indica s indice,
# sino su valor

lista.remove('alendi')
print(lista)

#1.07 .clear() -> elimina todo los elementos de la lista

#lista.clear()

#1.08 .sort -> ordena todos los elementos de la lista (menor a mayor)
'''no funciona con cadenas de texto (strings)'''

lista1 = [456, 32874, False, True, False, 75834]

lista1.sort()
print(lista1)

'''si utilizamos sort(reserve = True) ordena los elementos
al revez, de mayor a menor'''

lista1.sort(reverse=True)
print(lista1)

#1.09 .reverse -> invierte los elementos de la lista

lista1.reverse()
print(lista1)

#1.11 .index -> verifica si un elemento se encuentra en la lista
'''nos indica el indice en donde se encuentra el elemento, si no 
lo encuentra nos saldra un excepcion en pantalla, si le pedimos un
elemento repetido, nos mostrara el del indice menor'''

print(lista1.index(False))
print()


########################################################## (THOMPSON)

#2.1 COPIAR UNA LISTA EJ:

listauno = [1,2,3,4]
listados = []

for i in listauno:
    listados.append(i)

listados.append(19)

print(listauno)
print(listados)

#listauno = listados -> ESTA MAL! ambas listas valdiran lo mismo


#2.2 Busqueda Secuencial: buscar un elemento indice por indice



for numero in range(0, len(listados)):
    print(numero) 










