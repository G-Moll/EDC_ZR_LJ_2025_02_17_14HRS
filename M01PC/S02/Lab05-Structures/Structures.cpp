#include <iostream>
#include <string>
using namespace std;


struct Student {
	string name;
	string lastname;
	int age;
	bool registered;
};

int main() {
	Student joshua;
	joshua.name = "Joshua";
	joshua.lastname = "Hernandez";
	joshua.age = 33;
	joshua.registered = true;
	cout <<
		joshua.name <<
		joshua.lastname <<
		joshua.age <<
		joshua.registered << endl;

	Student john;
	john.name = "John";
	john.lastname = "Perez";
	john.age = 40;
	john.registered = false;
	cout <<
		john.name <<
		john.lastname <<
		john.age <<
		john.registered << endl;
	
    return 0;
}
