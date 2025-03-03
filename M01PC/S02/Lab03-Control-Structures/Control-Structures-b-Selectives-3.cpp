#include <iostream>
using namespace std;

int main() {

    int choice = 0;
    switch( choice ) {
        case -2:
        case -1:
        case 0:
            cout << "El valor está en el rango del -2 al 0" << endl;
            break;
        case 1:
        case 2:
        case 3:
            cout << "El valor está en el rango del 1 al 3" << endl;
            break;
        case 4:
        case 5:
        case 6:
            cout << "El valor está en el rango del 4 al 6" << endl;
            break;
        default:
            cout << "Tu numero está fuera del rango" << endl;
    }

    return 0;
}
