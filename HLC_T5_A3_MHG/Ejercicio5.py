def frecuencia_palabras():
    frase="El código es correcto"
    palabras=frase.split()
    frecuencia={}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            print (frecuencia)
        
        return frecuencia
    
frecuencia_palabras()

