#include <iostream>
#include <climits>
using namespace std;

int main() {
int  t ; cin>>t;
while(t--){
    
    int n ; cin>>n;
    int arr[n];
    for (int i=0;i<n;i++){
        cin>>arr[i];
    }
    
    
    int min = INT_MAX;
    int idx=0;
    
    for(int i=0;i<n;i++){
        if(arr[i]<min) {min=arr[i];
            idx=i;
        }
        
    }
    
    int sum=0;
    for(int i=0;i<n;i++){
        if(i!=idx) sum+=arr[i];
        
    }
    cout<<sum<<endl;
}

}

