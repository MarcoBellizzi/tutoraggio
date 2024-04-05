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


# scrivere una funzione che ricevuto un numero restituisca vero se
# il numero è pari, falso altrimenti
def verifica_pari(x):
    if x % 2 == 0:
        return True
    else:
        return False


# scrivere una funzione che ricevuti due numeri ritorni vero se almeno
# uno dei due è pari, falso altrimenti
def verifica_almeno_un_pari(x, y):
    if x % 2 == 0 or y % 2 == 0:
        return True
    return False


# scrivere una funzione che ricevuti 3 numeri ritorni vero se la somma dei primi due 
# è divisibile per il terzo, falso altrimenti
def verifica_condizione(x, y, z):
    return (x + y) % z == 0
    

### ESERCIZI MEDI - LEZIONE 3 E 4 ###


# scrivere una funzione che ricevuta una lista di numeri ritorni il maggiore
def massimo_in_lista(lista):
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max


# scrivere una funzione che ricevuto un numero verifichi se è primo
def numero_primo(numero):
    condizione = True
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            condizione = False
    return condizione


# scrivere una funzione che ricevuta una parola verifichi se sia palindroma
def verifica_palindroma(parola):
    palidroma = True
    for i in range(len(parola) // 2):
        if parola[i] != parola[len(parola) - i - 1]:
            palidroma = False
    return palidroma


# scrivere una funzione che ricevute due parole verifichi se tutte le lettere 
# nella prima compaiono nella seconda
def verifica_lettere(parola1, parola2):
    condizione = False
    for i in range(len(parola1)):
        if i in parola2:
            condizione = True
    return condizione


# una funzione che stampi il numero delle vocali in una frase
def stampa_numero_vocali(frase):
    cont = 0
    for lettera in frase:
        if lettera == 'a' or lettera == 'e' or lettera == 'i' or lettera == 'o' or lettera == 'u':
            cont += 1
    print('il numero di vocali è', cont)


# scrivere una funzione che ricevuta una lista di numeri verifichi se esistono 
# due numeri vicini la cui somma è un numero pari
def somma_vicini_pari(lista):
    condizione = False
    for i in range(len(lista) - 1):
        if (lista[i] + lista[i+1]) % 2 == 0:
            condizione = True
    return condizione


# scrivere una funzione che ricevuta una parola ritorni la lettera più frequente
def lettera_più_frequente(parola):
    cont_max = 0
    char_max = ""
    for carattere in parola:
        cont = 0
        for carattere2 in parola:
            if carattere == carattere2:
                cont += 1
        if cont > cont_max:
            cont_max = cont
            char_max = carattere

    return char_max


# una funzione che ricevute una parola e una lista di parole, verichi se tutte le lettere delle
# prima parola compaiono almeno una volta in ogni parola nella lista

# input : 'ab' , ['marco', 'francesco', 'python']

def verifica_presenza_caratteri(parola, lista):
    bol = True
    for lettera in parola:
        for parola2 in lista:
            if lettera not in parola2:
                bol = False
    return bol


### ESERCIZI DIFFICILI - LEZIONE 5 e 6 ###


# scrivere una funzione che ricevuta una matrice la stampi al contrario (da sotto 
# a sopra e da destra a sinistra)
def stampa_matrice_al_contrario(matrice):
    for i in range(len(matrice), -1, -1):
        for j in range(len(matrice[i]), -1, -1):
            print(matrice[i][j], end=" ")
        print()


# scrivere una funzione che ricevuta una matrice di numeri, stampi la somma dei numeri pari
def somma_numeri_pari(matrice):
    somma = 0
    for riga in matrice:
        for elemento in riga:
            if elemento % 2 == 0:
                somma += elemento
    print(somma)


# scrivere una funzione che ricevuti due parametri R e C crei e ritorni 
# una matrice R x C con valori crescenti da 0
def crea_matrice(righe, colonne):
    matrice = []
    cont = 0
    for i in range(righe):
        riga = []
        for j in range(colonne):
            riga.append(cont)
            cont += 1
        matrice.append(riga)
    return matrice


# scrivere una funzione che ricevuta una matrice la stampi a scacchiera
def stampa_matrice_a_scacchiera(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if (i + j) % 2 == 0:
                print(matrice[i][j], end=" ")
            else:
                print("  ", end=" ")
        print()


# scrivere una funzione che ricevuta una matrice verifichi se in ogni riga
# ci sono tutti elementi diversi
def elementi_diversi_in_righe(matrice):
    condizione = True
    for i in range(len(matrice)):
        for x in range(len(matrice[i])):
            for y in range(len(matrice[i])):
                if x != y and matrice[i][x] == matrice[i][y]:
                    condizione = False
    return condizione


# scrivere una funzione ricorsiva che verifichi se in una matrice ci sono solo elementi positivi
def condizione_ricorsiva(matrice, i, j):
    # caso base - positivo (se ho visitato tutte le celle)
    if i == len(matrice):
        return True
    # caso base - negativo (trovo una cella con valore negativo)
    if matrice[i][j] < 0:
        return False
    # caso ricorsivo - se sono sull'ultima colonna mi sposto una riga in basso e torno sulla prima colonna
    if j == len(matrice[0]) -1:
        return condizione_ricorsiva(matrice, i+1, 0)
    # caso ricorsivo - se non sono sull'ultima colonna mi sposto di una cella a destra
    return condizione_ricorsiva(matrice, i, j+1)