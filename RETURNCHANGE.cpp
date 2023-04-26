#include <iostream> 
using namespace std; 
int round(int n) 
{ 
    int a = (n / 10) * 10; 
    int b = a + 10; 
   
    return (n - a > b - n)? b : a; 
} 

int main() { 
int t; 
cin>>t; 
while(t--){ 
     int x; 
     cin>>x; 
     cout<<round(100-x)<<endl; 
} 
return 0; 
} 
