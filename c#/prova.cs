using System;

namespace NamespaceProva {

    class Prova {

        public static int getNumeroRandom() {
            Random random = new Random();
            int numero = random.Next(0, 10);
            return numero;
        }

        public static bool pari(int numero) {
            return numero % 2 == 0;
        }

        static void Main(string[] args) {
            
            int numero = getNumeroRandom();

            Console.WriteLine(numero);

            if (pari(numero)) {
                Console.WriteLine("è pari");
            } else {
                Console.WriteLine("non è pari");
            }

        }
    }
}