from libro import Libro
from autor import Autor
import unittest

def get_list(nombre_fichero_palabras):
    f = open(nombre_fichero_palabras + ".txt", mode="rt", encoding="utf-8")
    texto = f.read()
    if (len(texto) == 0):
        raise ValueError("El texto está vacío")
    diccionario = {}
    lista = texto.split(" ")
    #lista = ["hola", "que", "tal", "h"] 
    contador_longitud_mayor = 0
    for palabra in lista:
        if(contador_longitud_mayor < len(palabra)):
            contador_longitud_mayor = len(palabra)
    for i in range(0, contador_longitud_mayor + 1):
        lista_llenar = []
        for palabra in lista:
            if(len(palabra) == i):
                lista_llenar.append(palabra)

        if(len(lista_llenar) >0):
            diccionario[i] = lista_llenar

    return diccionario

def mas_antiguos(lista_libros, anyo):
    if (anyo < 1900 or anyo > 2021):
        raise ValueError("El año no es válido")

    lista_return = []
    for libro in lista_libros:
        if ((libro.get_anyo() <= anyo) == True):
            lista_return.append(libro.get_titulo())

    return lista_return

class Pruebas(unittest.TestCase):
    def libro_anyadido_titulo_igual(self):
        autor = Autor("4926", "Juan", "Tortosa")
        libro1 = Libro(autor, "titulo1", 2000)
        lista = [libro1]
        lista_prueba = mas_antiguos(lista, 2005) 
        self.assertEqual(lista_prueba[0], libro1.get_titulo())

    def test_comprobar_anyo(self):
        autor = Autor("4926", "Juan", "Tortosa")
        libro1 = Libro(autor, "titulo1", 2000)
        lista = [libro1]
        self.assertRaisesRegex(ValueError, "El año no es válido", mas_antiguos, lista, 2022 )

    def test_comprobar_tamanyo_lista(self):
        autor = Autor("4926", "Juan", "Tortosa")
        libro1 = Libro(autor, "titulo1", 2000)
        libro2 = Libro(autor, "titulo2", 2000)
        libro3 = Libro(autor,"titulo3", 2010)
        lista = [libro1,libro2,libro3]
        lista_prueba = mas_antiguos(lista, 2005)
        self.assertEqual(len(lista_prueba), 2) 





    

    
#---------------------main-------------------
"""
#print(get_list("documento_lista"))
autor = Autor("4926", "Juan", "Tortosa")
libro1 = Libro(autor, "titulo1", 2000)
libro2 = Libro(autor, "titulo2", 2000)
libro3 = Libro(autor,"titulo3", 2010)
lista = [libro1,libro2,libro3] 

lista_prueba = mas_antiguos(lista, 2005)
print(lista_prueba)
"""
print(get_list("documento_lista"))
if __name__ == "__main__":
    unittest.main()