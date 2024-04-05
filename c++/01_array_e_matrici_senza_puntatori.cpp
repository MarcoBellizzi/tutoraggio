#include <iostream>

using namespace std;


// In c++ la gestione di liste e matrici nelle funzioni soffre di un vincolo : non 
// è possibile recuperare la dimenzione di un array in una funzione (a meno che non si conosca gia
// a tempo di compilazione). Si può comunque passare come parametro, però funziona solo con gli
// array; con le matrici non è nemmeno possibile questo;


void stampa_array(int array[], int n) {
    for (int i=0; i<n; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

// void stampa_matrice(int matrice[][], int n, int m) {   // non ammesso
//     for (int i=0; i<n; i++) {
//         for (int j=0; j<m; j++) {
//             cout << matrice[i][j] << " ";
//         }
//         cout << endl;
//     }
// }


int main() {

    int n = 10;

    // dichiarazione array
    int array[n];
    
    // riempimento array
    for (int i=0; i<n; i++) {
        array[i] = i;
    }

    // stampa array
    stampa_array(array, n);

    cout << endl;


    // dichiarazione matrice
    int matrice[n][n];

    // riempimento matrice
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            matrice[i][j] = (i*n) + j;
        }
    }

    // stampa matrice
    // stampa_matrice(matrice, n, n);  // non ammesso
    for (int i=0; i<n; i++) {
        stampa_array(matrice[i], n);
    }

    return 0;
}