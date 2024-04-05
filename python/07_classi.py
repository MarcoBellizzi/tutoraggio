### CLASSI ###

# Le classi sono strumenti molto utili quando all'interno del tuo programma c'è la
# necessità di gestire molti elementi simili tra loro. Creare una classe 
# significa creare un nuovo tipo di variabile con il quale poter costruire oggetti complessi. 
# Ogni oggetto è formato da un insieme di variabili dette campi e un insieme di funzioni 
# dette metodi. Le classi hanno un metodo speciale detto costruttore che permette
# di costruire l'oggetto specificandone i campi e assegnandogli un valore iniziale.
# I metodi sono funzioni che ogni oggetto possiede e che mette a disposizione che 
# solitamente interagiscono con i campi per effettuare delle operazioni specifiche.

class Guerriero:

    # costruttore con valori di default dei campi
    def __init__(self, nome='marco', vita=100, attacco=10):
        # campi
        self.nome = nome
        self.vita = vita
        self.attacco = attacco

    # metodo senza parametri
    def stampa(self):
        # accedo ai campi dell'oggetto stesso
        print('mi chiamo', self.nome, 'e sono un guerriero normale')
        print('ho', self.vita, 'punti vita e', self.attacco, 'punti attacco', '\n')

    # metodo con un altro guerriero come parametro
    def attacca(self, guerriero):
        # decremento la vita dell'oggetto passato come parametro
        guerriero.vita -= self.attacco
        # accedo sia al proprio campo vita che a quella dell oggetto passato come parametro
        print(self.nome, "ha attaccato", guerriero.nome, '\n')


# costruisco un'istanza della classe guerriero (oggetto) usando il costruttore
marco = Guerriero()

# invoco il metodo stampa() dell'oggetto 
marco.stampa()

# costruisco un'altro oggetto (passandogli dei valori per i campi)
lorenzo = Guerriero(nome='lorenzo', attacco=20)

# stampo l'altro oggetto
lorenzo.stampa()

# invoco il metodo attacca() di marco passandogli come parametro l'oggetto lorenzo
marco.attacca(lorenzo)

# verifico che effettivamente il campo vita dell'oggetto lorenzo sia decrementato
lorenzo.stampa()




### EREDITARIETA' ###

# E' possibile creare una nuova classe a partire da un'altra, eredidandone tutte le 
# funzionalità implementate (campi e metodi) e avendo la possibilità di aggiungerne di nuove.
# E' possibile sia aggiungere nuovi campi e nuovi metodi, sia sovrascrivere quelli
# precedentemente implementati.


# creo una classe che eredita da (o estende) la classe guerriero
class GuerrieroSpeciale(Guerriero):

    # sovrascrivo un metodo esistente
    def stampa(self):
        print('mi chiamo', self.nome, 'e sono un guerriero speciale')
        print('ho', self.vita, 'punti vita e', self.attacco, 'punti attacco', '\n')

    # aggiungo un nuovo metodo
    def onda_energetica(self, guerriero):
        guerriero.vita -= self.attacco * 2
        print(self.nome, 'ha usato l\'onda energetica contro', guerriero.nome, '\n')
        

# creo un guerriero speciale usando il costruttore ereditato da guerriero
goku = GuerrieroSpeciale(nome='goku')

# verifico che il metodo stampa sia stato sovrascritto
goku.stampa()

# invoco il nuovo metodo aggiunto
goku.onda_energetica(marco)

# accedo direttamente al campo vita dell'oggetto marco
print('la vita di marco è', marco.vita)