#include <iostream>
using namespace std;

int main() {
    int T; 
    cin>>T; 
    while(T--){
        float N,X;
        cin>>N>>X;
        if(X>=N/2) {
        cout<<"YES"<<endl;
        }
        else {
        cout<<"NO"<<endl;
        }
    }
  return 0;
}