def nota(estudiantes):

    suma_calificacion = 0
    mejor_estudiante = ""
    mejor_calificacion = 0

    for nombre, calificacion in estudiantes.items():
        suma_calificacion += calificacion 
        if calificacion > mejor_calificacion:  
            mejor_calificacion = calificacion
            mejor_estudiante = nombre

    promedio=suma_calificacion/len(estudiantes)

    return f"Promedio:{promedio:.2f}, Mejor estudiante: {mejor_estudiante} con {mejor_calificacion}"

estudiantes = {'Juan': 6, 'Ana': 9, 'Pedro': 7}
resultado = nota(estudiantes)
print(resultado)