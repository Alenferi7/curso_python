#1.Metodos en cadena

#DATO IMPORTANTE
#Funcion -> FUNCION(dato)
#Metodo -> dato.metodo(parametros o no)

cadena1 = 'Hola soy Alen'
cadena2 = 'Bienvenido :)'
cadena3 = 'vegetta777'
cadena4 = '45454653 '
cadena5 = 'H05k'

#1.2 DIR -> devuelve la lista de atributos validos del objeto/tipo 
#dato pasado

print (dir(cadena1))

#########################################################################

#1.2 UPPER -> convierte en mayuscula

print (cadena1.upper())

#1.3 Lower -> convierte en miniscula

print (cadena2.lower())

#1.4 Capitalize -> primera en mayuscula

print (cadena3.capitalize())

#########################################################################

#1.5 Find -> encuentra la primera aparicion del valor especificado,
#sino devuelve -1

print (cadena1.find(' Alen'))

'''me devuele la ubicacion del dato que solicite, sino devulve -1,
en el caso que sea un string con mas de 1 palabra, me devuelve en donde
se encuentra la primera'''

#1.6 Index -> encuentra la primeta aparicion del valor especificado,
#sino devuelve una excepcion

print (cadena3.index('77'))

#########################################################################

#1.7 Isnumeric -> si es numerico devuleve True

print (cadena4.isnumeric())

#1.8 Isalpha -> si es alfa numerico decuelve True

print (cadena5.isalpha())

'''Los espacios no son alfanumericos'''

#########################################################################

#1.9 Count -> devuelve el numero de ocrrencias de una subcadena dada

print (cadena1.count('l'))

#1.10 Len -> cuenta los caracteres de una cadena
#Len no es un metodo, es una funcion!

print (len(cadena1)) 

#########################################################################

#1.11 Startswith -> verifica si una cadena empieza con ...

print (cadena1.startswith('OLA'))

#1.12 Endswith -> verifica si una cadena termina con

print (cadena4.endswith(' '))

#1.13 Replace -> reemplaza un pedazo de la cadena dada, por otra dada
'''Recibe dos parametros, el primero es la cadena vieja que queremos
reemplazar, y el segundo es la nueva cadena que queremos elegir'''

print (cadena3.replace('vegetta', 'willyrex'))

#1.14 separa, en forma de lista, cadenas con la cadena que le pasemos
#como referente

print(cadena1.split(' '))


