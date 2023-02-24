'''a) diferencia en porcentaje entre el curso actual y:
- el mas rapido de los cursos
- el mas lento de otros cursos
- el promedio de los cursos'''

def porcentaje(a,b):
    resultado = 100 - a / b * 100
    return resultado

def diez_horas(x):
    resultado = (666.6 * x) / 100
    return resultado

este_curso = 1.5
curso_rapido = 2.5
curso_promedio = 4
curso_lento = 7

este_rapido = porcentaje(este_curso, curso_rapido)
este_promedio = porcentaje(este_curso, curso_promedio)
este_lento = porcentaje(este_curso, curso_lento)

print (f"Este curso dura un {este_rapido}% menos que el mas rapido")
print (f"Este curso dura un {este_promedio}% menos que el promedio")
print (f"Este curso dura un {este_lento}% menos que el mas lento")

'''b) porcentaje de material inservible que se reduce en:
- el promedio de los cursos
- el curso actual (este curso)'''
print()

este_curso_crudo = 3.5
curso_promedio_crudo = 5

este_horas_reducidas = porcentaje(este_curso, este_curso_crudo)
promedio_horas_reducidas = porcentaje(curso_promedio, curso_promedio_crudo)


print(f'Este curso editado, reduce un {este_horas_reducidas}% del total')

print(f'Los promedios editados, reducen un {promedio_horas_reducidas}% del total')

'''c) ver 10hs de este crso a cuantas de otros cursos equivale?
y al reves?'''

print()

diez_horas_rapido = diez_horas(curso_rapido)
diez_horas_promedio = diez_horas(curso_promedio)
diez_horas_lento = diez_horas(curso_lento)

print(f'10hs de este curso, equivaldrian a {diez_horas_rapido}hs del curso rapido')
print(f'10hs de este curso, equivaldrian a {diez_horas_promedio}hs del curso promedio')
print(f'10hs de este curso, equivaldrian a {diez_horas_lento}hs del curso lento')
