#include <iostream>
using namespace std;

int main() {
  int u;
  cin>>u;
  while(u--){
      int f;
      cin>>f;
      
      if(f==0){
          cout<<1<<endl;
          continue;
      }
      cout<< 2*f + f<<endl;
  }
  return 0;
}
