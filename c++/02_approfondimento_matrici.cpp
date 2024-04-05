#include <iostream>

using namespace std;

int main() {

	int n = 3;
	int cont = 0;
    int matrice[n][n];


	// caso da sinistra a destra, da sopra a sotto
	for(int i=0; i<n; i++) {  // blocchi la riga 
		for(int j=0; j<n; j++) {  // ti sposti sulle colonne
			matrice[i][j] = cont++;
		}
	}
	// 0 1 2
	// 3 4 5
	// 6 7 8 


	// caso da sinistra destra, da sotto a sopra
	for(int i=n-1; i>=0; i--) {  // blocchi la riga
		for(int j=0; j<n; j++) {  // ti sposti sulle colonne
			matrice[i][j] = cont++;
		}
	}
	// 6 7 8
	// 3 4 5
	// 0 1 2  
	

	// caso da destra a sinistra, da sopra a sotto
	for(int i=0; i<n; i++) {  // blocchi la riga
		for(int j=n-1; j>=0; j--) {  // ti sposti sulle colonne
			matrice[i][j] = cont++;
		}
	}
	// 2 1 0
	// 5 4 3
	// 8 7 6 


	// caso da destra a sinistra, da sotto a sopra
	for(int i=n-1; i>=0; i--) {  // blocchi la riga
		for(int j=n-1; j>=0; j--) {  // ti sposti sulle colonne
			matrice[i][j] = cont++;
		}
	}
	// 8 7 6  
	// 5 4 3
	// 2 1 0 




	// caso da sopra a sotto, da sinistra a destra
	for(int j=0; j<n; j++) {  // blocchi la colonna
		for(int i=0; i<n; i++) {  // ti sposti sulle righe
			matrice[i][j] = cont++;
		}
	}
	// 0 3 6
	// 1 4 7
	// 2 5 8 


	// caso da sopra a sotto, da destra a sinistra
	for(int j=n-1; j>=0; j--) {  // blocchi la colonna
		for(int i=0; i<n; i++) {  // ti sposti sulle righe
			matrice[i][j] = cont++;
		}
	}
	// 6 3 0
	// 7 4 1
	// 8 5 2 


	// caso da sotto a sopra, da sinistra a destra
	for(int j=0; j<n; j++) {  // blocchi la colonna
		for(int i=n-1; i>=0; i--) {  // ti sposti sulle righe
			matrice[i][j] = cont++;
		}
	}
	// 2 5 8
	// 1 4 7
	// 0 3 6 


	// caso da sotto a sopra, da destra a sinistra
	for(int j=n-1; j>=0; j--) {  // blocchi la colonna
		for(int i=n-1; i>=0; i--) {  // ti sposti sulle righe
			matrice[i][j] = cont++;
		}
	}
	// 8 5 2
	// 7 4 1
	// 6 3 0 




	// stampa la matrice normalmente
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			cout << matrice[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}
