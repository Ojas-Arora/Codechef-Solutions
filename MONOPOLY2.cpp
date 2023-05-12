#include <iostream>
using namespace std;

int main() {
 int T;
 cin>>T;
 while(T--){
     int A,B,C,D;
     cin>>A>>B>>C>>D;
     if((A+B+C)<D || (A+B+D)<C || (A+C+D)<B || (B+C+D)<A){
         cout<<"YES"<<endl;
     }
     else{
         cout<<"NO"<<endl;
     }
 }
 return 0;
}
