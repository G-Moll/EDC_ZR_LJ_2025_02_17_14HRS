#include <iostream>
using namespace std;

int main() {
    // INE number, District number
    int ine_number = 234;
    int district_number = 78;

    // Validate INE number & District number
    if( ine_number > 0 && district_number == 20 ) {
        cout << "Puedes votar" << endl;
        cout << "Has votado" << endl;
        cout << "Te han marcado el pulgar" << endl;
    }
    else {
        cout << "No puedes votar" << endl;
    }
    return 0;
}
