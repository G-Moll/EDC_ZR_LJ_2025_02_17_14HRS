#include <iostream>
using namespace std;

int main() {
    //                   0    1    2    3    4    5
    char alphabet[] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
    //                  0   1    2   3   4
    cout << alphabet[ 0 ] << endl;
    cout << alphabet[ 6 ] << endl;

    for( int i = 0; i < 26 ; i++ ) {
     cout << "index "<< i << ": " << alphabet[ i ] << endl;
    }

    int numbers[] = { -10, 15, -20, 20, 28, 0, -5, 7, 3, 37 };
    for( int n = 0; n < 10; n++ ) {
        if( numbers[ n ] >= 0 ) {
            cout << numbers[ n ] << " es positivo" << endl;
        }
        else {
            cout << numbers[ n ] << " es negativo" << endl;
        }
    }
    return 0;
}
