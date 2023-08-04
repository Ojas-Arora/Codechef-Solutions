#include <iostream>
using namespace std;

int main() {

    int A,B,X,Y;
    cin>>A>>B>>X>>Y;
    int M=2*A+B;
    int R=2*X+Y;
    if (M>R)
        cout<<"Messi"<<endl;
    else if (M==R)
        cout<<"Equal"<<endl;
        else
            cout<<"Ronaldo"<<endl;

	return 0;
}
