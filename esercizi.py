### ESERCIZI BASE - LEZIONI 1 E 2 ###

# scrivere una funzione che ricevuti due numeri ritorni il maggiore
def massimo_tra_due_numeri(x, y):
    if x > y:
        return x
    else:
        return y
    

# scrivere una funzione che ricevuti tre numeri ritorni il maggiore
def massimo_tra_tre_numeri(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z


# scrivere una funzione che ricevuto un numero restituisca vero se il numero è pari, falso altrimenti
def verifica_pari(x):
    if x % 2 == 0:
        return True
    else:
        return False


# scrivere una funzione che ricevuti due numeri ritorni vero se almeno uno dei due è pari, falso altrimenti
def verifica_almeno_un_pari(x, y):
    if x % 2 == 0 or y % 2 == 0:
        return True
    return False


# scrivere una funzione che ricevuti 3 numeri ritorni vero se la somma dei primi due è divisibile per il terzo, falso altrimenti
def verifica_condizione(x, y, z):
    return (x + y) % z == 0
    

### ESERCIZI MEDI - LEZIONE 3 ###


# scrivere una funzione che ricevuta una lista di numeri ritorni il maggiore
def massimo_in_lista(lista):
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max


# scrivere una funzione che ricevuta una parola verifichi se sia palindroma
def verifica_palindroma(parola):
    palidroma = True
    for i in range(len(parola) // 2):
        if parola[i] != parola[len(parola) - i - 1]:
            palidroma = False
    return palidroma


### ESERCIZI DIFFICILI ###