#include <iostream>
#include <cmath>

using namespace std;

int main(){
    unsigned int N, A, B;
    unsigned long long result=0;
    cin>>N;
    unsigned int* Q = new unsigned int[N];
    unsigned int* C = new unsigned int[N];
    for(int i = 0; i < N; i++){
        cin>>Q[i];
    }
    for(int i = 0; i < N; i++){
        cin>>C[i];
    }
    cin>>A>>B;


    double phi;
    if(A!=B){
        phi=1/2.;
    }
    else{
        phi = 0;
    }

    for(int i = 0; i < N; i++){
        if(A<B){
            result+=static_cast<unsigned long long>(Q[i])*ceil((B-A)*(C[i])/255.+A);
        }
        else{
            result+=static_cast<unsigned long long>(Q[i])*A;
        }
    }

    cout<<result;
    delete[] Q;
    delete[] C;
    return 0;
}
