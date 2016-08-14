print("""\
Program that asks the user for a number n and gives him the possibility to choose between computing the sum and computing the product of 1,...,n.
Created By Keyvin Duque <thkeyduq@gmail.com>
""")

n = int(input('Ingrese un numero: '))
choice = input('Desea usted realizar la suma o la multiplicacion de sus elementos? (s para suma, m para multiplicacion): ')
salida = 'Opcion incorrecta, debe ingresar "s" para suma y "m" para multiplicacion'
resultado = None

if choice == 's':
    salida = "La suma de sus elementos es:"
    resultado = 0
    for i in range(1, n + 1):
        resultado += i
elif choice == 'm':
    salida = "La multiplicacion de sus elementos es:"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

print(salida, resultado if resultado is not None else "")