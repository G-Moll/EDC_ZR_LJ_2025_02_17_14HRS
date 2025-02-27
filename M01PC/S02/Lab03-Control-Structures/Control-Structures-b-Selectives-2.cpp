#include <iostream>
using namespace std;

int main() {

    char choice = '8';
    switch( choice ) {
        case 'x':
            cout << "Desplazamiento horizontal" << endl;
            break;
        case 'y':
            cout << "Desplazamiento vertical" << endl;
            break;
        case 'z':
            cout << "Desplazamiento en profundidad" << endl;
            break;
    }

    return 0;
}
