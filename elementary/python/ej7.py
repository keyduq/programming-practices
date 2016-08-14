print("""\
Write a program that prints a multiplication table for numbers up to 12.
Created By Keyvin Duque <thkeyduq@gmail.com>
""")

for i in range(1, 13):
    print('-- Tabla de', i, '--')
    for j in range(1, 13):
        print(i, 'x', j, '=', i*j)
    print('')