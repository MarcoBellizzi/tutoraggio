### STRINGHE ###


# le stringhe sono semplicemente delle variabili il cui contenuto è una sequenza di caratteri.
x = 'bracadabra'

# possiamo vedere una stringa come una lista di caratteri (non si possono usare i metodi visti prima però).

# usare la funzione len per sapere la dimensione della stringa.
print(len(x))

# scorrere una stringa.
for carattere in x:
    print(carattere)

# accedere ad un singolo carattere.
quarto_carattere = x[3]
print(quarto_carattere)

# usare gli slicer.
sottostringa = x[2:6]
print(sottostringa)

# con le stringhe possiamo usare gli operatori di confronto visti precedentemente con i numeri.
# gli operatori == e != ritornano vero o falso a secondo se le due stringhe sono uguali o diverse
# mentre gli operatori >, >=, <, <= rispettano l'ordine alfabetico.
print("java" != "python")
print("albero" < "balena")

# possiamo usare l'operatore + per concatenare due stringhe.
x = "questa è u" + "na stringa conc" + "atenata"
print(x)

# possiamo usare l'operatore * per duplicare una stringa più volte.
x = "ciao " * 3
print(x)

# il metodo split() serve per dividere una stringa in parole e metterle in una lista.
x = "ciao mi chiamo marco"
parole = x.split()
print(parole)

# i numeri possono essere trasformati in stringhe e viceversa.
x = 5
x = str(x)
x += "1"
print(x)

x = "5"
x = int(x)
x += 1
print(x)