#include <iostream>
using namespace std;

int main() {
    // int choice = 3; // 1, 2, 3
    // switch( choice ) {
    //     case 1:
    //         cout << "El valor en el num 1" << endl;
    //         break;
    //     case 2:
    //         cout << "El num 2 es el seleccionado" << endl;
    //         break;
    //     case 3:
    //         cout << "Ahora es el tercer valor" << endl;
    //         break;
    //     default:
    //         cout << "No coincide tu numero" << endl;
    // }

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
