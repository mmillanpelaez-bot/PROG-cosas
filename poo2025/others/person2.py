# poo = Programa Orientado a Objetos
# __init__ = initialize
class Person2:

    def __init__(self, name: str, age: int, dni: str):
        self.set_name(name)
        self.set_age(age)
        self.set_dni(dni)


    def set_name(self, name: str):
        self._name = name

    def set_age(self, age: int):

        if 0 > age > 150:
            raise ValueError("ERROR: Introduce una edad valida.")

        self._age = age


    def set_dni(self, dni):

        if len(dni) != 9:
            raise ValueError("ERROR: El DNI debe tener 9 caracteres.")

        if not dni[:8].isdigit():
            raise ValueError("ERROR: Los primeros 8 caracteres del DNI deben ser numeros.")

        if not dni[-1:].isalpha():
            raise ValueError("ERROR: El ultimo carcater del DNI debe ser una letra.")

        letter_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        calculation = int(dni[:-1]) % 23

        if letter_dni[calculation] != dni[-1:].upper():
            raise ValueError("ERROR: Introduzca un DNI existente.")

        self._dni = dni


    def __str__(self):
        string = (f"name: {self.name}\n "
                  f"age: {self.age}\n "
                  f"dni: {self.dni}\n "
                  f"adress:{self.adress}\n "
                  f"nacionality: {self.nacionality}")
        return string

    def __eq__(self, other): # eq = equal
        return self.dni == other.dni

    def __gt__(self, other): # gt = greater than
        return self.age > other.age

    def __lt__(self, other): # ls = less than
        return self.age < other.age

    #__eq__
    #__lt__
    #__gt__
    #__le__
    #__ge__
    #__ne__