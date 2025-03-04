#include <iostream>
using namespace std;

int main() {

    for( int i = 0; i < 1000; i++ ) {
        cout << "for: " << i << endl;
        if( i == 3 ) {
            break;
        }
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
