### ESERCIZI BASE ###

# scrivere una funzione che ricevuti due numeri ritorni il maggiore
def massimo_tra_due_numeri(x, y):
    if x > y:
        return x
    else:
        return y


# scrivere una funzione ricevuto un numero ritorni True se il numero è pari, False altrimenti
def pari(x):
    if x % 2 == 0:
        return True
    else:
        return False


# scrivere una funzione che ricevuti tre numeri ritorni il maggiore
def massimo_tra_tre_numeri(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
    

### ESERCIZI MEDI ###


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