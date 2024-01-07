### INTRODUZIONE ###


# Pe linee che iniziano con un # sono dei commenti e non fanno parte del programma.

# Per eseguire un programma python bisogna inizialmente installare python sul prorpio computer.
# (https://www.aranzulla.it/come-installare-python-1210886.html)

# Consiglio poi di installare il programma Visual Studio Code per creare ed eseguire programmi.
# (https://www.andreaminini.com/visualstudio/come-installare-visual-studio-code-sul-pc)

# Per creare una programma python bisogna creare un file il cui nome finisce con l'estenzione .py
# (esempio 'programma.py') e scrivere il codice del programma al suo interno.

# Per eseguire un programma bisogna aprire un terminale, posizionarsi nella cartella in cui 
# si trova il file python e digitare il comando 'python programma.py'.

# Maggiori informazioni su come usare il terminale possono essere trovate qui.
# (https://www.html.it/pag/393132/command-prompt-windows-introduzione/)


### VARIABILI ###


# Una varibile rappresenta una scatola, ha un tipo, un nome e un contenuto (o valore).
# Esistono vari tipi di variabili, ad esempio numeriche e alfanumeriche (dette stringhe).

# x è una variabile numerica il cui contenuto è il numero 5.
x = 5

# nome è stringa (ovvero una sequenza di caratteri).
nome = 'marco'


### INTERAZIONI CON IL TERMINALE ###


# E' possibile interagire con il terminale attraverso dei comandi (o funzioni).

# La funzione print() serve per scrivere qualcosa sul terminale.

# è' possibile scrivere sia stringhe
print('ciao')

# sia numeri
print(3)

# sia variabili, delle quali verrà stampato il contenuto.
x = 3
print(x)

# è possibile inserire varie cose (separate da virgola) che verranno 
# stampate una dopo l'altra.
print('stringa', 3)

# La funzione input() serve per leggere dal terminale qualcosa.

# tra le parentesi è possibile inserire una frase che verrà visualizzata nel terminale.
nome = input('come ti chiami? ')
print('ciao', nome)

# possiamo controllare il tipo di una variabile attraverso la funzione type()
var = 'parola'
print(type(var))

# di default la funzione input() considera cioè che legge come una stringa. 
stringa = input()
print(type(stringa))

# E' possibile convertire il tipo di una variabile attraverso le funzioni int() e str().

# leggiamo un numero
x = int(input())
print(type(x))

# convertiamo un numero in una stringa
x = str(3)
print(type(x))


### OPERATORI ARITMETICI ###


# In python sono ammesse tutte le operazioni aritmetiche.

# operatore somma.
x = 2
y = 3
z = x + y
print(z)

# operatore sottrazione.
x = 5 - 1
print(x)

# operatore moltiplicazione.
x = 8 * 3
print(x)

# operatore divisione.
print(10 / 3)

# operatore divisione intera (non prende la parte decimale ma solo la parte intera).
print(10 // 3)

# operatore modulo (è il resto della divisione).
print(7 % 2)

# operatore incremento (aggiunge un valore ad una variabile).
x = 5
x += 1  # uguale ad x = x + 1
print(x)

# operatore decremento (sottrae un valore ad una variabile).
x = 4
x -= 2  # uguale ad x = x - 2
print(x)

# operatore moltiplicazione e assegnamento (moltiplica una variabile per un valore).
x = 2
x *= 3
print(x)

# operatore divisione e assegnamento (divide una variabile per un valore).
x = 6
x /= 3
print(x)

# operatore divisione intera e assegnamento (divide interamente una variabile per un valore).
x = 10
x //= 3
print(x)

# operatore modulo e assgnamento
x = 10
x %= 3
print(x)


### FUNZIONI ###


# E' possibile creare nuove funzioni. Creare una funzione è un modo 
# per racchiudere un blocco di codice da poter usare in seguito.

# una funzione può (ma non obbligatoriamente) avere un insieme di parametri che riceve come input,
# esse sono delle varibili che la funzione riceve dall'esterno e che può usare al proprio interno. 

# una funzione può (ma non obbligatoriamente) avere un valore di ritorno, ovvero un valore
# che restituisce in output all'esterno dopo aver eseguito il blocco di codice all'interno.

# il codice che va eseguito all'interno della funzione va messo con un tab di spazio dopo 
# la dichiarazione della funzione

# creazione di una funzione senza parametri e senza valore di ritorno.
def saluta():
    print('questa stampa viene dalla funzione')
    print('ciao marco')

# chiamata alla funzione.
saluta()

# creazione di una funzione con una parametro e senza valore di ritorno.
def stampa_numero_al_quadrato(x):
    print(x * x)

stampa_numero_al_quadrato(4)

# creazione di una funzione che ha come parametri due numeri e che ha come valore di ritorno la loro somma.
def somma_due_numeri(x, y):
    z = x + y
    return z

x = somma_due_numeri(5, 7)
print(x)