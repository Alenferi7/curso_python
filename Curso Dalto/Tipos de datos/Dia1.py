#1.Tipos de dato simples 

#1.1 strings

string = 'Hola mundo'

string2 = 'Mundo hola'

string3 = string + string2

print(string, string2, string3)

#1.2 ints

ints = 19

ints2 = 7

ints3 = 19 + 7

print(ints, ints2, ints3)

#1.3 True/False

True
False

#2.Tipos de datos compuestos

#2.1 listas []

lista = []

lista.append(50)

print(lista)

#2.2 tuplas () 

tupla = ('Hola', 'Mundo', 'Alen', 70.6)

print(tupla)

'''las tuplas no se puede modificar, solo restaurar 
(eliminar todos los datos y agregar nuevos). Ejs:'''

'''tupla.append('Holis mundo')'''
'''tupla[3] = 78534'''

#2.3 conjuntos (set) {}

conjuntos = {'Mirko', 22, 'Franco', 18, 'Alen', 21, 'Miranda', 19, 'Miranda',19}

print(conjuntos)

'''Los conjuntos no muestran en pantalla datos duplicados, 
tripiclados, etc..'''
'''Tampoco puede acceder a elemtos por el indice, Ej.'''
'''print(conjunto[3])'''
'''Ni se modifican'''
'''conjuntos[2] = 45'''
'''No tienen un orden'''
print(conjuntos)


#2.4 diccionarios {}

diccionario = {'nombre': 'Alen ferinovic', 'edad': 20, 'altura': 1.95, 'peso': '70kg'}

print(diccionario)
print(diccionario['nombre'],)

aloha = input('Que dato requiere: ')

print(diccionario[aloha])

'''Guardan un valor y una clave, podemos acceder al valor
preguntando por la clave (diccionatio['nombre']) = Alen'''

#Operadores aritmeticos



