//Ball Distribution
#include <iostream> 
#include <vector> 
using namespace std; 
 
int main() { 
    int T; 
    cin >> T; 
 
    while (T--) { 
        int N, M; 
        cin >> N >> M; 
 
        vector<int> B(M); 
        for (int i = 0; i < M; i++) { 
            cin >> B[i]; 
        } 
 
        int Sum = 0; 
        for (int i = 0; i < M; i++) { 
            Sum += N - B[i]; 
        } 
 
        cout << max(0, N - Sum) << endl; 
    } 
 
    return 0; 
}
