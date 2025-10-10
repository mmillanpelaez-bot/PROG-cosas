#verify if leap year (el año debe ser divisible por 4, pero no por 100, a menos que también sea divisible por 400)
def leap_year(year):
    if (year % 4 == 0 and year % 100 !== 0) or (year % 400 == 0):
        return True