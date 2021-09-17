from os import system
from time import sleep

def crear_matriu(mida):
    matriu = []
    for i in range(mida):
        matriu.append([' ' for x in range(mida)])
    matriu[mida // 2][mida // 2] = 'x'
    matriu[mida // 2 - 1][mida // 2] = 'x'
    matriu[mida // 2][mida // 2 - 1] = 'x'
    matriu[mida // 2 - 1][mida // 2 - 1] = 'x'
    return matriu

def mostra_matriu(matriu):
    for i in range(len(matriu)+2):
        print('=', end = '')
    print()
    for i in range(len(matriu)):
        print('|', end = '')
        for z in range(len(matriu[0])):
            print(matriu[i][z], end = '')
        print('|')
    for i in range(len(matriu)+2):
        print('=', end = '')
    print()

def mostrar_efecte(matriu):
    while True:
        system('cls')
        sleep(1)
        mostra_matriu(matriu)
        for i in range(len(matriu)//2-1):
            matriu[i][i], matriu[i+1][i+1] = matriu[i+1][i+1], matriu[i][i]
        for i in range(len(matriu)//2-1):
            matriu[len(matriu)-1-i][i], matriu[len(matriu)-2-i][i + 1] = matriu[len(matriu)-2-i][i + 1], matriu[len(matriu)-1-i][i]
        for i in range(len(matriu) - 1, len(matriu)//2, -1):
            matriu[i][i], matriu[i - 1][i - 1] = matriu[i - 1][i - 1], matriu[i][i]
        for i in range(len(matriu)//2-1):
            matriu[i][len(matriu)-1-i], matriu[i + 1][len(matriu)-2-i] = matriu[i + 1][len(matriu)-2-i], matriu[i][len(matriu)-1-i]




matriu = crear_matriu(6)
mostrar_efecte(matriu)