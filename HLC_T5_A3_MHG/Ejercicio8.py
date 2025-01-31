def vocal_consonante():
    frase= 'hola mundo'
    vocales=['a','e','i','o','u']
    contador_vocales=0
    contador_consonantes=0
    
    for i in frase:
        if i in vocales :
            contador_vocales+=1
        else:
            contador_consonantes+=1
    print('Vocales',contador_vocales,'Consonantes',contador_consonantes)
          
vocal_consonante()