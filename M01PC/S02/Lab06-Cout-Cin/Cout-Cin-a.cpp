#include <iostream>
#include <string>
using namespace std;

int main() {
    // Strings
    string name;
    string hobby;

    cout << "Type your name: ";
    cin >> name;
    cout << "Type your hobby: ";
    cin >> hobby;

    cout << "Your name is " + name + " and your hobby is " + hobby << endl;
    return 0;
}
