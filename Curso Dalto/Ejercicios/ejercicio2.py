'''a) pedirle al usuario que diga cualquier texto real y:
- calcular cuanto tardaria en decir esa frase
- cuantas palabras dijo?'''

'''b) si se tarda mas de 1 minuto:
- decirle: hablas demasiado'''

def palabras_segundos (b):
    resultado = len(b) / 2
    return resultado

def palabras_martina (y):
    resultado = (70 * y) / 100
    return resultado


texto = input('Ingrese un texto real: ')
lista = texto.split()

segundos = palabras_segundos(lista)

if segundos >= 60:
    print('Para! estas hablando demasiado')
else:
    print(f'Dijiste un total de {len(lista)} palabras y tardaste {segundos} sengundos')

'''c) Martina habla un 30% mas rapido: cuanto tardaria en decirlo?'''

martina = palabras_martina(segundos)

print(f'Martina enves de tardar {segundos} segundos, va a tardar {martina} segundos.')




