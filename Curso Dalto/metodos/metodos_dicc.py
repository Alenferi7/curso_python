#1. Metodos diccionarios.

diccionario = {'nombre': 'Alen', 'edad': 20, 'profesion': 'Programador'}

#1.01 .Keys() -> devuelve claves

print(diccionario.keys())

#1.02 .get() -> develve el valor de una clave
'''no lanza excepciones. diccionario['jkfaj'], nos lanzara una excepcion'''

print(diccionario.get('nombre'))

#1.03 .clear() -> elimina todos los elementos

#diccionario.clear()

#1.04 .pop() -> elimina un elemento

diccionario.pop('nombre')

print(diccionario)

#1.05 .items() -> para iterar el dict

print(diccionario.items())


