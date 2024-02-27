# scrivere una funzione ricorsiva che cerca un numero in un matrice, e se lo trova restistuisce
# true se non lo trova ritorna False

import random

def cerca_valore(matrice, numero, riga, colonna):
    # primo caso base - trovo il numero
    if matrice[riga][colonna] == numero:
        return True
    
    # secondo caso base - ho analizzato tutti i numeri e non ho mai trovato il numero
    if riga == len(matrice) - 1 and colonna == len(matrice[riga]) - 1:
        return False

    # primo caso ricorsivo - vai a destra
    if colonna != len(matrice[riga]) - 1:
        return cerca_valore(matrice, numero, riga, colonna + 1)

    # secondo caso ricorsivo - vai sotto
    if colonna == len(matrice[riga]) - 1:
        return cerca_valore(matrice, numero, riga + 1, 0)


matrice = []

for i in range(10):
    riga = []
    for j in range(10):
        riga.append(random.randint(1, 100))
    matrice.append(riga)

print(matrice)

numero = 50

if cerca_valore(matrice, numero, 0, 0):
    print('ho trovato il numero', numero)
else:
    print('non ho trovato il numero', numero)