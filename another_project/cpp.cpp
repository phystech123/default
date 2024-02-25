#include<iostream>
using namespace std;
int fact(int a);
int main(){
    int t;
    cin>>t;
    cout<<fact(t);
    return 0;
}
int fact(int a){
    int s=1;
    for(int i=1; i<=a; i++){
        s*=i;
    }
    return s;
}