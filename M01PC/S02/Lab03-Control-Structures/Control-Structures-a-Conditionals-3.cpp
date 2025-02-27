#include <iostream>
using namespace std;

int main() {

    int x = 20;
    int y = 10;

    if( x == y ) {
        cout << "Son iguales" << endl;
    }
    else if( x <= y ) {
        cout << "x si es menor o igual que y" << endl;
    }
    else if( y != y ) {
        cout << "y si es diferente que y" << endl;        
    }
    else {
        cout << "y no es diferente que y" << endl;        
    }

    return 0;
}
