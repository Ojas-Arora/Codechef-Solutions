#include <iostream>
using namespace std;

int main() {
    int T;
    cin>>T;
    while(T--){
        int A,B,C;
        cin>>A>>B>>C;
        if (C==A+B) {
            cout<<"YES"<<endl;
        }
        else {
            cout<<"NO"<<endl;
        }
    }
	return 0;
}
