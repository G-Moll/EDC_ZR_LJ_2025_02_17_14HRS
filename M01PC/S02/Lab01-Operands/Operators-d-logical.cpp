#include <iostream>
using namespace std;

int main() {
	// LOGICAL OPERATORS
	cout << "t1 and t2 and t3: " <<
	  ( 1 == 2 and 2 == 3 and 3 == 4 ) << endl;
	cout << "t1 and t2 and t3: " <<
	  ( 1 == 1 and 2 == 3 and 3 == 4 ) << endl;
	cout << "t1 and t2 and t3: " <<
	  ( 1 == 1 and 2 == 2 and 3 == 4 ) << endl;
	cout << "t1 and t2 and t3: " <<
	  ( 1 == 1 and 2 == 2 and 3 == 3 ) << endl;

	cout << "t1 or t2 or t3: " <<
	  ( 1 == 2 or 2 == 3 or 3 == 4 ) << endl;
	cout << "t1 or t2 or t3: " <<
	  ( 1 == 1 or 2 == 3 or 3 == 4 ) << endl;
	cout << "t1 or t2 or t3: " <<
	  ( 1 == 1 or 2 == 2 or 3 == 4 ) << endl;
	cout << "t1 or t2 or t3: " <<
	  ( 1 == 1 or 2 == 2 or 3 == 3 ) << endl;

	cout << "true: " << true << endl;
	cout << "false: " << false << endl;
	cout << "! true: " << ! true << endl;
	cout << "! false: " << ! false << endl;
	cout << "!! true: " << !! true << endl;
	cout << "!! false: " << !! false << endl;
    
    return 0;
}
