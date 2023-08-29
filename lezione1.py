# le linee che iniziano con un # sono dei commenti, vengono ignorate dal computer.

# per eseguire un file python bisogna installare python sul prorpio computer.
# consiglio poi di installare il programma Visual Studio Code per creare ed eseguire i file.
# per eseguire un file bisogna aprire il terminale, posizionarsi sulla cartella in cui si trova il file
# ed eseguire il comando "python nome_file.py" in cui nome_file è proprio il nome che
# avete dato al file.


### VARIABILI ###


# una varibile è come una scatola, ha un nome e un contenuto.
# x è una variabile il cui contenuto è il numero 5.
x = 5

# il comando (o funzione) print() serve per scrivere sul terminale qualcosa.
# in questo caso stampiamo il contenuto della variabile x.
print(x)

# il comando (o funzione) input() serve per leggere dal terminale qualcosa.
# tra le parentesi è possibile inserire una frase che verrà visualizzata nel terminale.
# nella funzione print() è possibile inserire varie cose che verranno stampate una dopo l'altra.
x = input("inserisci dalla tastiera un numero : ")
print("il numero che hai inserito è", x)

# il contenuto delle variabili può variare durante l'esecuzione del programma.
# aggiorniamo il contenuto della variabile x.
x = 3
print(x)
x = 7
print(x)


### OPERATORI ARITMETICI ###


# in python sono ammesse tutte le operazioni aritmetiche.

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
x += 1
print(x)

# operatore decremento (sottrae un valore ad una variabile).
x = 4
x -= 2
print(x)

# operatore moltiplicazione e assegnamento (moltiplica una variabile per un valore).
x = 2
x *= 3
print(x)

# operatore divisione e assegnamento (divide una variabile per un valore).
x = 9
x /= 3
print(x)


### FUNZIONI ###


# creare una funzione in python è un modo per racchiudere un blocco di codice
# da poter chiamare ovunque, similmente alla funzione print().

# una funzione può (ma non obbligatoriamente) avere un insieme di parametri che riceve come input,
# esse sono delle varibili che la funzione riceve dall'esterno e che può usare al proprio interno. 

# una funzione può (ma non obbligatoriamente) avere un valore di ritorno, ovvero un valore
# che restituisce in output all'esterno dopo aver eseguito il blocco di codice all'interno.

# il codice che va eseguito all'interno della funzione va messo con un tab di spazio dopo 
# la sua dichiarazione

# creazione di una funzione senza parametri e senza valore di ritorno.
def saluta():
    print("questa stampa viene dalla funzione")
    print("ciao marco")

# chiamata alla funzione.
saluta()

# creazione di una funzione con una parametro e senza valore di ritorno.
def stampa_numero_al_quadrato(x):
    print(x * x)

stampa_numero_al_quadrato(4)

# creazione di una funzione che ha come parametri due numeri e che ha come valore di ritorno la loro somma.
def somma_due_numeri(primo_numero, secondo_numero):
    x = primo_numero + secondo_numero
    return x

x = somma_due_numeri(5, 7)
print(x)