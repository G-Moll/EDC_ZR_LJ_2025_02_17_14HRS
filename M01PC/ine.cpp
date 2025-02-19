#include <iostream>
using namespace std;

int main() {
	cout << "CPP App" << endl; // Sentence

	// ine number, district number
	int ine_number = 234;
	int district_number = 78;

	// Valite INE & District
	if( ine_number > 0 && district_number == 20 ) {
		cout << "Puede votar" << endl;
		cout << "Has votado" << endl;
		cout << "Te han marcado el pulgar" << endl;
	}
	else {
		cout << "No puedes votar" << endl;
	}
	return 0;
}
