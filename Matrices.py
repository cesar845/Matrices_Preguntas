matriz1 = [['✈︎','✈︎','✈︎','✈︎','✈︎'],
          ['✈︎','✈︎','✈︎','✈︎','✈︎'],
          ['✈︎','✈︎','✈︎','✈︎','✈︎'],
          ['✈︎','✈︎','✈︎','✈︎','✈︎'],
          ['✈︎','✈︎','✈︎','✈︎','✈︎']]

correcto = '☁︎'
incorrecto = '⛈︎'
ls_preguntas = ['¿Que es Python?\n1. Juego\n2. Lenguaje de programacion\n3. Marca de auto\n4. Ninguna de las anteriores',
                '¿Que es HTML?\n1. Lenguaje de maquetacion\n2. Marca de gaseosa\n3. Navegador\n4. Perro caliente',
                '']

ls_respuesta = ['2','1']

def fnt_pintarmatriz():
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            print(matriz1[i][j], end='  ')
        print()
sw = True
contador = 0

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        import os
        os.system('cls')
        fnt_pintarmatriz()
        print()
        print(ls_preguntas[contador])
        print()
        r = input('- >')
        if r == ls_respuesta[contador]:
            matriz1[i][j] = correcto
        else:
            matriz1[i][j] = incorrecto
        contador += 1