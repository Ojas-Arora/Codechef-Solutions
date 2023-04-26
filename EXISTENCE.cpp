#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        unsigned long long  x,y;
        cin>>x>>y;
        if((x*x*x*x+4*y*y)==(4*x*x*y))
         cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
 return 0;
}
