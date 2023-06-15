### MATRICI ###


# le matrici concettualmente rappresentano delle tabelle, formate da righe e colonne.
# più tecnicamente in python una matrice consiste in una lista di liste.
# c'è una lista principale che racchiude altre liste, ognuna della quali rappresenta una riga

# creazione di una matrice 3 x 3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# prendiamo la prima riga
prima_riga = matrice[0]
print(prima_riga)

# per capire BENE come scorrere le matrici osserviamo la differenza tra questi due
# modi di scorrere una lista

lista = [1, 2, 3, 4, 5]

# in questo caso cicliamo direttamente sugli elementi della lista.
# la variabile elemento contiene direttamente gli elementi della lista
for elemento in lista:
    print(elemento)

# in quest'altro caso usiamo le funzioni range() e len() per creare
# un insieme di indici degli elementi della lista
for indice in range(len(lista)):
    print(lista[indice])

# possiamo quindi usare quest'altro approccio per scorrere gli elementi di una matrice
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(matrice[i][j])

# notiamo come l'indice i scorre sulle righe della matrice mentre l'indice j
# scorre sulle colonne di ogni riga, dunque l'elemento matrice[i][j] rappresenta
# la cella alla riga i e alla colonna j

# creazione di una matrice 4 x 4 con celle uguali X
matrice = []
for i in range(4):
    matrice.append([])
    for j in range(4):
        matrice[i].append("X")

# stampa della matrice in formato tabella
# il parametro end=" " nella funzione print serve per non andare a capo dopo una stampa
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(matrice[i][j], end=" ")
    print("")
