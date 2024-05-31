#include <iostream>
using namespace std;
class fentree{
    public:
    int n, m;
    int foo(){
        cin >>n>>m;
        int arr[n+1];
        int maxx[n+1];

        for(int i = 1; i<=n; i++){
            cin>>arr[i];
        }

        for (int i = 1; i < n+1; i++){
            int xx = -1000000;
            int j = i&(i + 1);
            for (int k = j; k <= i; k++){
                xx = max(xx, arr[k]);
            maxx[i] = xx;
            }
        
        }   

        for (int i = 1; i < m+1; i++){
            int l, r;
            cin  >> l  >> r;
            int ma = -1000000;
            while (r&(r+1) >= l){
                ma = max(ma, maxx[r]);
                r= r&(r+1);
            }
            while (l|(l+1) <= r){
                ma = max(ma, maxx[l]);
                l = l|(l+1);
            }
            cout<< ma;
        }
        return 0;
    }
};

int main(){
    fentree tr;
    tr.foo();
}