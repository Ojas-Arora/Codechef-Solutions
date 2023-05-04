#include <bits/stdc++.h>
using namespace std;
int main() {
    int T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        int a1=INT_MIN,a2=INT_MIN;
        for(int i=0;i<n;i++){
            if(arr[i]>a1){
                a2=a1;
                a1=arr[i];
            }
            else{
                if(arr[i]>a2 && arr[i]!=a1){
                    a2=arr[i];
                }
            }
        }
        cout<<a1+a2<<endl;
    }
    return 0;
}