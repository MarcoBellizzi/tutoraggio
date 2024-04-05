#include <iostream>

using namespace std;


void stampa_array(int* array, int n) {
    for (int i=0; i<n; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

void stampa_matrice(int** matrice, int n, int m) {
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cout << matrice[i][j] << " ";
        }
        cout << endl;
    }
}


int main() {

    int n = 10;

    // dichiarazione di un array
    int* array = new int[n];

    // riempimento array
    for (int i=0; i<n; i++) {
        array[i] = i;
    }

    // stampa array
    stampa_array(array, n);

    cout << endl;


    // dichiarazione matrice
    int** matrice = new int*[n];
    for (int i=0; i<n; i++) {
        matrice[i] = new int[n];
    }

    // riempimento matrice
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            matrice[i][j] = (i*n) + j;
        }
    }

    // stampa matrice
    stampa_matrice(matrice, n, n);

    return 0;
}