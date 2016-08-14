import random

print("""\
A guessing game where the user has to guess a secret number. After every guess the program tells the user whether 
their number was too large or too small. At the end the number of tries needed should be printed. 
I counts only as one try if they input the same number multiple times consecutively.
Created By Keyvin Duque <thkeyduq@gmail.com>
""")

min, max = 1, 99
randNumber = random.randrange(min, max);
maxIntentos = 20
ingresados = []
intentos = 0
finded = False
print('Posee %d intentos para adivinar el numero, el numero se encuentra entre %d y %d' % (maxIntentos, min, max))

while intentos < maxIntentos:
    n = int(input('Ingrese un numero a adivinar: '))
    if n < min or n > max:
        print('Solo puedes ingresar numeros entre %d y %d' % (min, max))
    elif n in ingresados:
        print('Ya has ingresado este numero')
    elif n == randNumber:
        finded = True
        break
    else:
        print('Estas cerca!' if n + 10 >= randNumber and n - 10 <= randNumber else 'Estas lejos!')
        ingresados.append(n)
        intentos += 1

print('Correcto! Has adivinado el numero!!' if finded else 'Se te acabaron los intentos')