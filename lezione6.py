### RICORSIONE ###

# la ricorsione è un processo in cui una funzione chiama se stessa.
# all'interno di una funzione ricorsiva troviamo due elementi chiave:
#   - il/i caso/i base: sono i casi in cui la catena di chiamate a se stessa si interrompe.
#   - il/ caso/i ricorsivo/i: sono i casi in cui invece la catena non si interrompe e viene effettuata
#       una nuova chiamata.

# facciamo un esempio di una funzione ricorsiva che stampi in maniera decrescente tutti i numeri
# più piccoli di una dato numero che prende come parametro. Notiamo che la funzione non ha valori di
# ritorno ma si limita a stampare una serie di numeri.

def ricorsione(n):
    # caso base
    if n == 0:
        print(n)
    # caso ricorsivo
    if n > 0:
        print(n)
        ricorsione(n-1)

ricorsione(7)

# facciamo ora un altro esempio e proviamo a creare una funzione ricorsiva che ritorni il fattoriale
# di un dato numero. Notiamo in questo caso che la funzione ha un valore di ritorno.

def fattoriale(n):
    # caso base
    if n == 2:
        return n
    # caso ricorsivo
    return n * fattoriale(n-1)

print(fattoriale(5))
