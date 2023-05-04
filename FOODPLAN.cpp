#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    
    while (T--) {
        int N, M;
        cin >> N >> M;
         double onlinefood = N - (0.1 * N);
        if (onlinefood < M) {
            cout << "ONLINE" << endl;
        } 
        else if (onlinefood > M) {
            cout << "DINING" << endl;
        } 
        else {
            cout << "EITHER" << endl;
        }
    }
    return 0;
}