class Libro:
    """Create an object Aircraft
    Args:
      registration: Is a code for the flight
      modelo: It is the type of model of the Aircraft
      num_rows: Is a number of the rows of the flight
      num_seats_per_row: Is a number of the seats for each row
    """
    def __init__(self):
        self.__registration = registration
        self.__model = modelo
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):
        return self.__registration

    def get_model(self):
        return self.__model
        

    def seating_plan(self):
        """Generates a seating plan for the number of rows and seats per row
        Returns:
        rows: A list of rows such as 1, 2, etc.
        seats: A string of letters such as 'ABCDEF'
        """
        lista_asientos_final = []
        lista_letras_abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        for i in range(0, self.__num_rows + 1):
            diccionario = {}
            for i in range(0, self.__num_seats_per_row):
                diccionario[lista_letras_abecedario[i]] = None
            lista_asientos_final.append(diccionario)
        lista_asientos_final[0] = None

        return lista_asientos_final

    def num_seats(self):
        """Calculates the number of seats
        Returns:
        seats: The number of seats
        """
        number_seats = self.__num_rows * self.__num_seats_per_row
        return number_seats
        

    