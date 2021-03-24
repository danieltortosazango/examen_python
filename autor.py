class Autor:
    """Create an object Autor
    Args:
    
    """
    def __init__(self,id_autor,nombre,apellido):
        self.__id_autor = id_autor
        self.__nombre = nombre
        self.__apellido = apellido

    def get_id_autor(self):
        return self.__id_autor

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido
        