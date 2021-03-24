from libro import Libro
from autor import Autor

def get_list(nombre_fichero_palabras):
    f = open(nombre_fichero_palabras + ".txt", mode="rt", encoding="utf-8")
    texto = f.read()
    diccionario = {}
    #if (len(texto))
    lista = ["hola", "que", "tal"]
    for palabra in lista:
        longitud_palabra = len(palabra)
        print(palabra)
        lista_palabras_misma_longitud = []

    
    return lista

def mas_antiguos(lista_libros, anyo):
    if (anyo < 1900 or anyo > 2021):
        raise ValueError("El año no es válido")

    lista_return = []
    for libro in lista_libros:
        if ((libro.get_anyo() <= anyo) == True):
            lista_return.append(libro.get_titulo())

    return lista_return

    
#---------------------main-------------------

#print(get_list("documento_lista"))
autor = Autor("4926", "Juan", "Tortosa")
libro1 = Libro(autor, "titulo1", 2000)
libro2 = Libro(autor, "titulo2", 2000)
libro3 = Libro(autor,"titulo3", 2010)
lista = [libro1,libro2,libro3] 

lista_prueba = mas_antiguos(lista, 2005)
print(lista_prueba)