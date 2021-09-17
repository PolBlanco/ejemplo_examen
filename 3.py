from random import randint, randrange
preguntes = ['Nom de tres capitals europees', 'Tres sinònims', 'Quadre i pintor', 'Monument i ciutat']
respostes = ['Madrid, Viena i Londres', 'Control, examen i test', "El Guernica i Pablo Picasso", "La Sagrada Familia i Barcelona"]

def a(llista1 = [], llista2 = []):
    dicc = {}
    for b in range(len(llista1)):
        dicc[llista1[b]] = llista2[b]
    return dicc

def b(stringako = ''):
    vocals = 'aeiou'
    escollides = ''
    while len(escollides) < 2:
        lletra = chr(randint(97,122))
        if lletra not in vocals and lletra not in escollides:
            escollides += lletra
    escollides += vocals[randint(0,4)]
    print('Les lletres triades són: ', end = '')
    for i in escollides:
        print(i, end = ' ')
    print()
    nou_string = ''
    for i in stringako:
        if i.lower() not in escollides and i not in ' ,':
            nou_string += '_'
        else:
            nou_string += i
    return nou_string

def main():
    dicc = a(preguntes,respostes)
    random = randrange(len(preguntes))
    resposta, pregunta = dicc[preguntes[random]], list(dicc.keys())
    pregunta = pregunta[random]
    print(f'La pregunta és {pregunta}')
    print(f'I la resposta a descubrir és: \n{b(resposta)}')

main()