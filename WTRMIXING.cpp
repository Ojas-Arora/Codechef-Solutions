#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin>>T;
    while(T--){
        int a,b,x,y;
        cin>>a>>b>>x>>y;
        int temp = (a-b);
        if(temp==0)
        cout<<"YES"<<endl;
        else if(temp<0){
            if(abs(temp)<=x)
            cout<<"YES"<<endl;
            else
            cout<<"NO"<<endl;
        }
        else{
            if(abs(temp)<=y)
            cout<<"YES"<<endl;
            else
            cout<<"NO"<<endl;
        }
    }
    return 0;
} 