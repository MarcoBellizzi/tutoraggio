### BOOLEANE ###


# oltre a numeri e stringhe, le variabili possono assumere valori booleani.
# una booleana è una variabile che ammette due possibili valori: vero o falso.

# x è una varibile booleana vera.
x = True

# x è una varibile booleana falsa.
x = False


### CONNETTORI ###


# i connettori mettono in relazione due o più booleane, al fine di stabilire il valore finale.

# il connettore and restituisce vero se tutte le varibili sono vere, falso altrimenti.
x = True
y = True
z = x and y
print(z)

x = True
y = x and False
print(y)

# il connettore or restituisce vero se c'è almeno una varibile vera.
x = True or False
print(x)

# i connettori possono essere combinati usando le parentesi tonde.
print((False or False) and True)


### OPERATORI DI CONFRONTO ###


# gli operatori di confronto confrontano due valori e restituiscono un valore booleano.

# l'operatore == restituisce vero se le due varibili sono uguali.
x = 5 == 7
print(x)

# l'operatore != restituisce vero se le due varibili sono diverse.
print(5 != 3)

# l'operatore > restituisce vero se la prima è maggiore della seconda.
print(5 > 3)

# l'operatore >= restituisce vero se la prima è maggiore o uguale della seconda.
print(5 >= 5)

# l'operatore < restituisce vero se la prima è minore della seconda.
print(5 < 3)

# l'operatore <= restituisce vero se la prima è minore o uguale della seconda.
print(5 <= 7)


### COSTRUTTI ###


# i costrutti sono degli strumenti per verificare il valore di verità di una booleana.

# il costrutto if serve per eseguire del codice solo se il valore booleano
# presente all'interno dell'if è vero.
# il codice che va eseguito se la condizione è vera va messo con un tab di spazio dopo l'if.
if 5 > 3:
    print('5 è maggiore di 3')

if 8 < 2:
    print('8 minore di 2')

# il costrutto else serve per eseguire del codice qualora il valore presente nell'if fosse falso.
if 5 <= 2:
    print('5 è minore o uguale di 2')
else:
    print('5 è maggiore di 2')

# il costrutto elif serve per porsi un ulteriore domanda qualora il valore presente nell'if fosse falso.
x = 5

if x < 3:
    print('x è minore di 3')
elif x < 7:
    print('x è compresa tra 3 e 7')
elif x < 10:
    print('x è compresa tra 7 e 10')
else:
    print('x è maggiore di 10')