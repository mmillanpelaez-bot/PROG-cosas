# verify date function
from os.path import split

def verify_date():
    # steps:
    #ask for a date and save as text
    date_str = (int(input("Enter date: (dd/mm/aaaa)")))
    #use split("/") to divide the text in a list
    split("/")
    # verify list has exactly 3char
    #verify format (dd/mm/aaaa)
    #verify length (10char)
    if len(date_str) == 10:
        print("correct date format")
    else:
        print("Invalid date format")
    #use isdigit to check whether each of the 3 elements is a number.
    #verify if leap year (el año debe ser divisible por 4, pero no por 100, a menos que también sea divisible por 400)
    def leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
    #verify

verify_date()