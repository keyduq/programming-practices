print("""\
Write a program that prints all prime numbers. 
(Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)
Created By Keyvin Duque <thkeyduq@gmail.com>
""")

n = int(input('Ingrese la cantidad de numeros primos que desea generar: '))
actual = 1 #numero que se va recorriendo
contador = 0

while contador < n:
    isPrime = True
    for i in range(2, actual):
        if actual % i == 0:
            isPrime = False
            break
    if isPrime:
        print(actual)
        contador += 1
    actual += 1
