### CLASSI ###

class Guerriero:

    # costruttore con valori di default dei parametri
    def __init__(self, nome='marco', vita=100, attacco=10):
        self.nome = nome
        self.vita = vita
        self.attacco = attacco

    # metodo senza parametri
    def stampa(self):
        print('mi chiamo', self.nome, 'e sono un guerriero normale')
        print('ho', self.vita, 'punti vita e', self.attacco, 'punti attacco', '\n')

    # metodo con un altro guerriero come parametro
    def attacca(self, guerriero):
        guerriero.vita -= self.attacco


guerriero = Guerriero()
guerriero.stampa()

guerriero2 = Guerriero(nome='lorenzo', attacco=120)
guerriero2.stampa()

guerriero.attacca(guerriero2)
guerriero2.stampa()


### EREDITARIETA' ###


print('--- ereditarieta ---', '\n')


# classe che estende la classe precedente
class GuerrieroSpeciale(Guerriero):

    # sovrascrivere un metodo esistente
    def stampa(self):
        print('mi chiamo', self.nome, 'e sono un guerriero speciale')
        print('ho', self.vita, 'punti vita e', self.attacco, 'punti attacco', '\n')

    # aggiungere un metodo
    def onda_energetica(self):
        print('-------> O', '\n')


guerriero_speciale = GuerrieroSpeciale()
guerriero_speciale.stampa()

guerriero.attacca(guerriero_speciale)
guerriero_speciale.stampa()

guerriero_speciale.onda_energetica()
