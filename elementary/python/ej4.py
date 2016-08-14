# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

n = int(input('Ingrese un numero: '))
total = 0
for i in range(n + 1):
    total += i
print('La suma total es:', total)