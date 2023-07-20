#include<bits/stdc++.h>
using namespace std;



void solve(){
 int X,Y,R;
 cin>>X>>Y>>R;
 int total = X+(R/30);

 if(total%Y > 1){
cout<<(total/Y) + 1<<endl;
 }
 else{
 cout<<(total/Y)+(total%Y)<<endl;
 }

}

int main(){
int T;
 cin>>T;
 while(T--){
solve();
 }
 return 0;
}
