#include <iostream>

using namespace std;


class Studente {

    // campi privati
    private:

        string nome;
        string cognome;
        int matricola;

    // metodi pubblici
    public:

        // costruttore senza parametri
        Studente() {
            (*this).nome = "marco";
            (*this).cognome = "bellizzi";
            (*this).matricola = 223966;
        };

        // costruttore con parametri
        Studente(string nome, string cognome, int matricola) {
            (*this).nome = nome;
            (*this).cognome = cognome;
            (*this).matricola = matricola;
        };

        // costruttore per copia
        Studente(const Studente& studente) {
            (*this).nome = studente.nome;
            (*this).cognome = studente.cognome;
            (*this).matricola = studente.matricola;
        };

        string getNome() {
            return (*this).nome;
        };

        string getCognome() {
            return (*this).cognome;
        };

        int getMatricola() {
            return (*this).matricola;
        };

        // override dell'operatore =
        Studente& operator=(const Studente& studente) {
            (*this).nome = studente.nome;
	        (*this).cognome = studente.cognome;
	        (*this).matricola = studente.matricola;
	        return *this;
        };

        // override dell'operatore ==
        bool operator==(const Studente& studente) {
            return (*this).nome == studente.nome &&
                (*this).cognome == studente.cognome &&
                (*this).matricola == studente.matricola;
        };

        void stampa() {
            cout << "nome : " << (*this).nome << endl;
            cout << "cognome : " << (*this).cognome << endl;
            cout << "matricola : " << (*this).matricola << endl;
        };

};


class Universita {

    private:

        string nome;

        // un array di studenti
        Studente* studenti;

        // un numero per sapere quanti studenti ci sono nell'array
        int dimenzione;

        // un numero per sapere la dimenzione dell'array
        int capacita;

    public:

        Universita() {
            (*this).nome = "unical";
            (*this).studenti = new Studente[10];
            (*this).dimenzione = 0;
            (*this).capacita = 10;
        };

        Universita(string nome, Studente* studenti, int dimenzione, int capacita) {
            (*this).nome = nome;
            (*this).studenti = new Studente[capacita];

            // copio gli studenti
            for (int i=0; i<dimenzione; i++) {
                (*this).studenti[i] = studenti[i];
            }

            (*this).dimenzione = dimenzione;
            (*this).capacita = capacita;
        };

        Universita(const Universita& universita) {
            (*this).nome = universita.nome;
            (*this).studenti = new Studente[universita.capacita];

            for (int i=0; i<universita.dimenzione; i++) {
                (*this).studenti[i] = universita.studenti[i];
            }

            (*this).dimenzione = universita.dimenzione;
            (*this).capacita = universita.capacita;
        };

        // distruttore
        ~ Universita () {
            delete[] studenti;
        };

        Universita& operator=(const Universita& universita) {

            (*this).nome = universita.nome;

            // dealloco la memoria precedentemente allocata
            delete[] (*this).studenti;

            // alloco nuova memoria
            (*this).studenti = new Studente[universita.capacita];

            for (int i=0; i<universita.dimenzione; i++) {
                (*this).studenti[i] = universita.studenti[i];
            }

            (*this).dimenzione = universita.dimenzione;
            (*this).capacita = universita.capacita;

            return *this;
        };

        const Studente& operator[](int i) {
            if (i >= 0 && i < (*this).dimenzione) {
                return (*this).studenti[i];
            }
            throw invalid_argument("l'indice non è valido");
        };

        void aggiungiStudente(const Studente& studente) {

            // se c'è ancora spazio nell'array lo aggiungo
            if ((*this).dimenzione < (*this).capacita) {
                (*this).studenti[(*this).dimenzione] = studente;
                (*this).dimenzione += 1;
            } else {
                // altrimenti creo un altro array di dimensione doppia, copio gli elementi
                // attuali, aggiungo lo studente e poi sposto il puntatore

                (*this).capacita *= 2;

                Studente* temp = new Studente[(*this).capacita];

                for (int i=0; i<(*this).dimenzione; i++) {
                    temp[i] = (*this).studenti[i];
                }
                
                temp[(*this).dimenzione] = studente;

                (*this).dimenzione += 1;

                delete[] (*this).studenti;

                (*this).studenti = temp;
            }

        };

        void stampa() {
            cout << "elenco degli studenti dell'universita " << (*this).nome << " :" << endl;
            for (int i=0; i<(*this).dimenzione; i++) {
                (*this).studenti[i].stampa();
            }
        };

};


int main() {

    // costruttore senza parametri
    Studente marco = Studente();

    // costruttore con parametri
    Studente francesco = Studente("francesco", "critelli", 123456);

    // costruttore per copia
    Studente copia = Studente(marco);

    // operatore ==
    if (marco == copia) {
        cout << "i due studenti sono uguali" << endl;
    }

    // operatore =
    copia = francesco;

    if (! (marco == copia)) {
        cout << "i due studenti non sono uguali" << endl;
    }


    Universita unical = Universita();

    unical.aggiungiStudente(marco);
    unical.aggiungiStudente(francesco);

    unical.stampa();

    return 0;
}