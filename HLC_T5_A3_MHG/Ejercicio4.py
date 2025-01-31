def sumaPromedio():
    numeros=[1,2,3,4,5]
    suma=0

    for i in numeros:
        suma=suma+i
        
    print("El resultado de la suma es", suma)
    print("El promedio es", suma/len(numeros))

sumaPromedio()