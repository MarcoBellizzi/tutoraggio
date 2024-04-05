#include <iostream>

using namespace std;

// introduzione ai puntatori
void introduzione_puntatori() {

    // dichiarazione di un puntatore
    int* p;

    // allocazione di un'area di memoria sufficiente per una variabile intera
    p = new int;

    cout << "indirizzo di memoria : " << p << endl;
    cout << "numero di bytes allocati : " << sizeof(p) << endl;
    cout << "numero di bytes per un numero intero : " << sizeof(int) << endl;
    cout << "valore iniziale : " << *p << endl << endl;

    // accedo all'elemento puntato dal puntatore p e modifico il contenuto
    *p = 10;

    cout << "valore : " << *p << endl << endl;

    // liberazione della memoria associata alla variabile puntatore
    delete p;

    cout << "indirizzo di memoria : " << p << endl;
    cout << "numero di bit allocati : " << sizeof(p) << endl;
    cout << "valore : " << *p << endl << endl;
}


void cambio_valore() {

    // dichiarazione di una variabile intera x
    int x = 5;

    // dichiarazione di un puntatore
    int* p;

    // faccio puntare p all'indirizzo di memoria in cui si trova x
    p = &x;

    // modifico il contenuto della memoria puntata da p
    *p = 10;

    // stampo il contenuto di x per verificare che il contenuto sia stato modificato
    cout << x << endl;
}


int main() {

    introduzione_puntatori();

    // cambio_valore();

    return 0;
}