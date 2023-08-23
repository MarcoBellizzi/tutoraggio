### LISTE ###

# le liste sono un insieme ordinato di elementi.

# creazione di una lista vuota.
lista = []

# creazione di una lista con elementi.
lista = [1, 7, 2, 4]

# gli elementi di una lista possono avere tipo diverso o anche essere altre liste.
lista = [1, False, [3, 4]]

# per accedere ad un elemento della lista si usano le parentesi quadre
# con il relativo indice all'interno (partendo da 0).
lista = [2, 4, 1, 3]
primo_elemento = lista[0]
print(primo_elemento)

secondo_elemento = lista[1]
print(secondo_elemento)

# si può prendere una determinata porzione della lista usando gli slicer (i due punti).
lista = [1, 2, 3, 7, 9, 12, 5, 8, 4, 6]

# prendiamo solo gli elementi compresi dal terzo al settimo.
porzione_lista = lista[2:7]
print(porzione_lista)

# la funzione len() restituisce la lunghezza della lista.
x = len(lista)
print(x)

# le liste hanno dei metodi con i quali è possibile interagire con gli elementi.

lista = [5, 7, 5, 12, 15]

# il metodo append() aggiunge un elemento in coda alla lista.
lista.append(3)
print(lista)

# il metodo insert() aggiunge un nuovo elemento nella posizione specificata.
posizione = 2
elemento = 8
lista.insert(posizione, elemento)
print(lista)

# il metodo remove() cerca e rimuove un elemento dalla lista.
# se ce n'è' più di uno, rimuove solo la prima occorrenza.
lista.remove(5)
print(lista)

# il metodo pop() rimuove l'elemento alla posizione specificata.
lista.pop(3)
print(lista)


### FOR ###


# il costrutto for serve per scorrere una lista e ripetere del codice per ogni elemento nella lista.
# il codice che va ripetuto va messo con un tab di spazio dopo il for.
lista = [1, 3, 4, 7]
for elemento in lista:
    print(elemento)

# notiamo che la funzione print() viene eseguita tante volte quanti sono gli elementi nella lista
# e che la variabile elemento assume ogni volta un valore diverso.

# la funzione range() serve per creare una lista di valori da usare in un ciclo for.

# creazione di numeri interi consecutivi a partire da 0 fino ad un valore specificato.
for elemento in range(10):
    print(elemento)

# creazione di numeri interi consecutivi a partire da un valore specificato fino ad un altro valore specificato.
for elemento in range(5, 10):
    print(elemento)

# creazione di numeri non cosecutivi ma separati da un intervallo.
for elemento in range(3, 15, 3):
    print(elemento)

# possiamo anche innestare due cicli for in questo modo.
for primo_elemento in range(3):
    for secondo_elemento in range(3):
        print(primo_elemento * secondo_elemento)


### WHILE ###


# il while() è un ciclo che a priori non sa quante volte ripetere il blocco di codice al suo interno,
# il codice verrà ripetuto fino al verificarsi di una condizione.

# riempiamo una lista con numeri letti da input finche non leggiamo il numero -1.
lista = []
x = input()
while x != -1:
    lista.append(x)
    x = input()
print(lista)

# la key word break serve per uscire immediatamente da un ciclo (sia for che while).

# stampiamo i numeri presenti in una lista finche non troviamo il numero -1
lista = [1, 2, 3, -1, 4, 5]
for elemento in lista:
    if elemento == -1:
        break
    print(elemento)