#include <bits/stdc++.h>
using namespace std;

int main() {

    int testCases;
    cin >> testCases;

    while (testCases--) {

        int length, width, side;
        cin >> length >> width >> side;


        int squareArea = side * side;

        int rectangleArea = length * width;

        
        if (rectangleArea <= squareArea) {
            cout << "0\n";
        } else {
            
            if (1 * width <= squareArea) {
                cout << "1\n";
            } else if (1 * length <= squareArea) {
                cout << "1\n";
            } else {

                cout << "2\n";
            }
        }
    }

    return 0;
}
