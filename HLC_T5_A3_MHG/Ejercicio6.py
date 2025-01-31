def clave_animales(lista_animales):
    diccionario = {palabra: len(palabra) for palabra in lista_animales}
    return diccionario

lista_animales = ["gato","perro","elefante"]

print(clave_animales(lista_animales))

