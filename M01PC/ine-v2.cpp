#include <iostream>
using namespace std;

int main() {
	// INE number, District number
	int ine_number = 234;
	int district_number = 78;

	// Validate INE number & District number
	cout << "::: VALIDANDO INE..." << endl;
	if( ine_number > 0 ) {
		cout << "Tu INE es valido" << endl;
		
		cout << "::: VALIDANDO DISTRITO..." << endl;
		if( district_number == 20 ) {
			cout << "Puedes votar" << endl;
			cout << "Has votado" << endl;
			cout << "Te han marcado el pulgar" << endl;
		}
		else {
			cout << "No puedes votar porque te corresponde otro distrito" << endl;
		}
	}
	else {
		cout << "No puedes votar porque tu INE no es valido" << endl;
	}
	return 0;
}
