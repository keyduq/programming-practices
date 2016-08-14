print("""\
A program that computes (ecuation on OneNote)
Created By Keyvin Duque <thkeyduq@gmail.com>
""")

sumatoria = 0

for k in range(1, 10 ** 6):
    sumatoria += ((-1) ** (k + 1)) / ((2 * k) - 1)

print('Resultado:', 4 * sumatoria)
print('Es pi jajajaja... mientras mas alto el final de la sumatoria, mas fiel el numero pi')