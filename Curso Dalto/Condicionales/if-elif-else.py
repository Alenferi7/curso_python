'''if condicion -> True:
    accion
else:
    accion'''

ingreso_menusual = int(input('Ingrese su ingreso menusual: '))

if ingreso_menusual >= 10000:
    print('Poder adquisitivo alto')

elif ingreso_menusual >= 5000:
    print('Clase media')

else:
    print('Situacion de pobreza')

'''el orden del if y elif lo tenes que pensar vos, porque el
interprete lee en cascada'''