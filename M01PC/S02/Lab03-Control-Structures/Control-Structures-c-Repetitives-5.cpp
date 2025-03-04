#include <iostream>
using namespace std;

int main() {

    for( int i = 0; i < 100; i++ ) {
        cout << "before: " << i << endl;
        if( i < 80 ) {
            continue;
        }
        cout << "after: " << i << endl;
    }

    for( int i = 0; i < 100; i++ ) {
        cout << "Proceso para todos los usuarios: " << i << endl;
        if( i % 5 != 0 ) {
            // 1 / 5, Cociente: 0, Residuo: 1
            // 2 / 5, Cociente: 0, Residuo: 2
            // 3 / 5, Cociente: 0, Residuo: 3
            // 4 / 5, Cociente: 0, Residuo: 4
            // 5 / 5, Cociente: 1, Residuo: 0
            continue;
        }
        cout << "PROCESO EXTRA: " << i << endl;
    }

    bool running = true;
    int counter = -20;
    while( running ) {
        cout << "Loop Running" << endl;
        if( counter == -18 ) {
            cout << "Broken Loop" << endl;
            break;
        }
        counter++;
    }

    int value = 10;
    do {
        cout << "Do while loop: " << value << endl;
        if( value > 1000000 ) {
            break;
        }
        value *= 10;
    }
    while( true );

    return 0;
}
