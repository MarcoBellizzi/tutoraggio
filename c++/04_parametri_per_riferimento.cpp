#include <iostream>

using namespace std;


// il parametro viene passato per copia
void modifica_valore_copia(int x) {
	x += 10;
}

// il parametro viene passato per riferimento
void modifica_valore_riferimento(int& x) {
    x += 10;
}

// il parametro viene passato tramite il suo puntatore
void modifica_valore_puntatore(int* x) {
    *x += 10;
}


int main() {
    
    int x = 5;

    cout << "x prima della funzione = " << x << endl; 

    modifica_valore_copia(x);  // non modifica il valore di x

    // modifica_valore_riferimento(x);  // modifica il valore di x

    // modifica_valore_puntatore(&x);  // modifica il valore di x
    
    cout << "x dopo la funzione = " << x << endl;

    return 0;
}