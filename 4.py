from time import sleep
from os import system
def abecedari(lletra):
    sleep(1)
    system('cls')
    print(chr(lletra))
    if lletra == 90:
        return abecedari(65)
    else:
        return abecedari(lletra+1)

abecedari(65)