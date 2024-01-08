//CARDSWIPE
#include <bits/stdc++.h> 
using namespace std; 
 
int main() { 
int T;
cin>>T; 
while(T--){ 
    int N; 
    cin>>N; 
    map<int,int> mp; 
    int c=0; 
    int ans=0; 
    for(int i=0;i<N;i++){ 
        int X;
        cin>>X; 
        mp[X]++; 
        if(mp[X]%2==1)
        c++; 
        if(mp[X]%2==0)
        c--; 
        ans=max(ans,c); 
          } 
    cout<<ans<<endl; 
    } 
 return 0; 
}