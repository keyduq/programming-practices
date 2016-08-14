from datetime import date

print("""\
A program that prints the next 20 leap years
Created By Keyvin Duque <thkeyduq@gmail.com>
""")

def esAnoBisiesto(ano):
    """Verifica si es un ano bisiesto"""
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    return False

year = date.today().year
contador = 0

print('Los proximos 20 anos bisiestos son los siguientes:')

while contador < 20:
    if esAnoBisiesto(year):
        print('El ano %d es bisiesto' % (year))
        contador += 1
    year += 1