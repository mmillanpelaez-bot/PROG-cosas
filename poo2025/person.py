# poo = Programa Orientado a Objetos
# __init__ = initialize
class Person:
    def __init__(self, name, age, dni, adress, nacionality):
        self.name = name
        if self.check_age(age):
            self.age = age
        else:
            self.age = 0
        if self.checkDni(dni):
            self.dni = dni
        else:
            self.dni = "00000000X"
        self.adress = adress
        self.nacionality = nacionality

    def check_age(self, age):
        if 0 <= age <= 150:
            return True
        else:
            return False

    def checkDni(self, dni):
        if len(dni) == 9 and dni[:1].isdigit() and dni[-1:].isalpha:
            letterDni = "TRWAGMYFPDXBNJZSQVHLCKE"
            return True

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